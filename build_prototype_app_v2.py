import os

def update_app():
    with open('/home/user/kdd-prototype/src/App.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState } from 'react';
import {
  INITIAL_DEVICES,
  INITIAL_RELAYS,
  INITIAL_SENSORS,
  INITIAL_CONTACTS,
  INITIAL_REMOTES,
  INITIAL_DEVICE_SETTINGS,
} from './mockData';

// Screens
import Screen01_Splash from './screens/Screen01_Splash';
import Screen02_MyDevices from './screens/Screen02_MyDevices';
import Screen03_RegisterStep1 from './screens/Screen03_RegisterStep1';
import Screen04_RegisterStep2 from './screens/Screen04_RegisterStep2';
import Screen05_RegisterStep3 from './screens/Screen05_RegisterStep3';
import Screen06_Dashboard from './screens/Screen06_Dashboard';
import Screen07_Settings from './screens/Screen07_Settings';
import Screen08_DeviceStatus from './screens/Screen08_DeviceStatus';
import Screen09_Outputs from './screens/Screen09_Outputs';
import Screen10_DeviceSettings from './screens/Screen10_DeviceSettings';
import Screen11_RemoteCoding from './screens/Screen11_RemoteCoding';
import Screen12_Remotes from './screens/Screen12_Remotes';
import Screen13_Contacts from './screens/Screen13_Contacts';
import Screen14_Sensors from './screens/Screen14_Sensors';
import DesignSpecView from './screens/DesignSpecView';

// Components
import BottomNavigation from './components/BottomNavigation';
import HardwareTerminal from './components/HardwareTerminal';
import NotificationDrawer from './components/NotificationDrawer';
import { playSound } from './utils/audio';
import {
  Smartphone,
  Layers,
  Shield,
  Battery,
  Signal,
  Wifi,
  ChevronDown,
} from 'lucide-react';

export default function App() {
  // Navigation & View Mode
  const [activeScreen, setActiveScreen] = useState('splash');
  const [viewMode, setViewMode] = useState('mobile'); // 'mobile' or 'spec'

  // Active Device & State
  const [devices, setDevices] = useState(INITIAL_DEVICES);
  const [activeDeviceId, setActiveDeviceId] = useState('kdd-fh500-0012');
  const [connectionMode, setConnectionMode] = useState('internet'); // 'internet' or 'sms'
  const [isArmed, setIsArmed] = useState(true);
  const [isAlarmActive, setIsAlarmActive] = useState(false);

  // Subsystems Data
  const [relays, setRelays] = useState(INITIAL_RELAYS);
  const [sensors, setSensors] = useState(INITIAL_SENSORS);
  const [contacts, setContacts] = useState(INITIAL_CONTACTS);
  const [remotes, setRemotes] = useState(INITIAL_REMOTES);
  const [deviceSettings, setDeviceSettings] = useState(INITIAL_DEVICE_SETTINGS);

  // Hardware Communication Logs
  const [hardwareLogs, setHardwareLogs] = useState([
    {
      time: '12:00:01',
      type: 'mqtt',
      direction: 'rx',
      payload: '{"device": "KDD-FH500-0012", "status": "ONLINE", "bat": 98, "gsm": 28, "armed": 1}',
      description: 'پکت وضعیت اولیه دریافتی از سرور ابری KDD',
    },
  ]);

  // Notifications / Event Logs
  const [events, setEvents] = useState([
    {
      time: '۱۰:۴۲',
      title: 'سیستم حفاظتی مسلح شد',
      message: 'توسط کاربر از طریق اپلیکیشن',
      level: 'info',
    },
    {
      time: 'دیروز ۱۸:۳۰',
      title: 'وضعیت باتری نرمال',
      message: 'سطح ولتاژ باتری نرمال (۱۲.۸ ولت)',
      level: 'info',
    },
  ]);
  const [notifDrawerOpen, setNotifDrawerOpen] = useState(false);

  // Registration Form State
  const [regForm, setRegForm] = useState({
    serial: 'KDD-FH500-0012',
    name: 'کامیون ولوو شماره ۱',
    simNumber: '09123456789',
    activeSim: 1,
    ownerName: 'علی احمدی',
    nationalId: '0012345678',
    ownerPhone: '09123456789',
    province: 'تهران',
    city: 'تهران',
    postalCode: '1234567890',
    technician: 'رضا محمدی (کد ۱۱۴)',
    password: '',
    confirmPassword: '',
    biometric: true,
  });

  const activeDevice = devices.find((d) => d.id === activeDeviceId) || devices[0];

  // Helper to log hardware commands
  const logCommand = (type, payload, description) => {
    const timeStr = new Date().toLocaleTimeString('fa-IR');
    setHardwareLogs((prev) => [
      ...prev,
      {
        time: timeStr,
        type,
        direction: 'tx',
        payload,
        description,
      },
    ]);
  };

  // 1. Arm / Disarm Toggle
  const handleToggleArm = () => {
    const nextState = !isArmed;
    setIsArmed(nextState);
    if (nextState) {
      playSound('arm');
      setIsAlarmActive(false);
      logCommand(
        connectionMode === 'sms' ? 'sms' : 'mqtt',
        connectionMode === 'sms' ? `SMS TO ${activeDevice.simNumber}: #ARM*1234#` : `MQTT TOPIC: kdd/${activeDevice.serial}/cmd -> {"action":"ARM","pass":"1234"}`,
        'فرمان مسلح‌سازی سیستم حفاظتی خودرو'
      );
      setEvents((prev) => [
        { time: 'همین الان', title: 'سیستم مسلح شد (ARM)', message: 'سیستم امنیتی توسط کاربر فعال گردید', level: 'info' },
        ...prev,
      ]);
    } else {
      playSound('disarm');
      setIsAlarmActive(false);
      logCommand(
        connectionMode === 'sms' ? 'sms' : 'mqtt',
        connectionMode === 'sms' ? `SMS TO ${activeDevice.simNumber}: #DISARM*1234#` : `MQTT TOPIC: kdd/${activeDevice.serial}/cmd -> {"action":"DISARM","pass":"1234"}`,
        'فرمان غیرمسلح‌سازی سیستم حفاظتی خودرو'
      );
      setEvents((prev) => [
        { time: 'همین الان', title: 'سیستم غیرمسلح شد (DISARM)', message: 'سیستم امنیتی موقتاً غیرفعال شد', level: 'warning' },
        ...prev,
      ]);
    }
  };

  // 2. Toggle Relay
  const handleToggleRelay = (relayId) => {
    setRelays((prev) =>
      prev.map((r) => {
        if (r.id === relayId) {
          const nextState = !r.state;
          logCommand(
            connectionMode === 'sms' ? 'sms' : 'mqtt',
            connectionMode === 'sms'
              ? `SMS TO ${activeDevice.simNumber}: #RELAY${relayId}=${nextState ? '1' : '0'}*1234#`
              : `MQTT: kdd/${activeDevice.serial}/relay -> {"relay":${relayId},"state":${nextState ? 1 : 0}}`,
            `تغییر وضعیت رله شماره ${relayId} (${r.name}) به ${nextState ? 'روشن' : 'خاموش'}`
          );
          return { ...r, state: nextState };
        }
        return r;
      })
    );
  };

  // 3. Pulse Relay
  const handlePulseRelay = (relayId) => {
    logCommand(
      connectionMode === 'sms' ? 'sms' : 'mqtt',
      connectionMode === 'sms' ? `SMS TO ${activeDevice.simNumber}: #PULSE${relayId}=2S*1234#` : `MQTT: kdd/${activeDevice.serial}/pulse -> {"relay":${relayId},"duration":2000}`,
      `تحریک لحظه‌ای ۲ ثانیه‌ای رله شماره ${relayId}`
    );
    setRelays((prev) =>
      prev.map((r) => (r.id === relayId ? { ...r, state: true } : r))
    );
    setTimeout(() => {
      setRelays((prev) =>
        prev.map((r) => (r.id === relayId ? { ...r, state: false } : r))
      );
    }, 2000);
  };

  // 4. Rename Relay
  const handleRenameRelay = (relayId, newName) => {
    playSound('click');
    setRelays((prev) =>
      prev.map((r) => (r.id === relayId ? { ...r, name: newName } : r))
    );
  };

  // 5. Change Relay Mode
  const handleChangeRelayMode = (relayId, newMode) => {
    playSound('click');
    setRelays((prev) =>
      prev.map((r) => (r.id === relayId ? { ...r, mode: newMode } : r))
    );
  };

  // 6. Trigger Sensor Test Simulation
  const handleTriggerSensor = (sensorId) => {
    playSound('alarm');
    setSensors((prev) =>
      prev.map((s) => (s.id === sensorId ? { ...s, isTriggered: true } : s))
    );
    setIsAlarmActive(true);
    logCommand(
      'sms',
      `INCOMING ALARM: SENSOR ${sensorId} TRIGGERED`,
      `شبیه‌سازی تحریک سنسور شماره ${sensorId}`
    );
    setEvents((prev) => [
      { time: 'همین الان', title: `تحریک سنسور شماره ${sensorId}`, message: 'هشدار امنیتی سنسور', level: 'alarm' },
      ...prev,
    ]);

    setTimeout(() => {
      setSensors((prev) =>
        prev.map((s) => (s.id === sensorId ? { ...s, isTriggered: false } : s))
      );
    }, 3500);
  };

  // 7. Sensor Settings
  const handleChangeSensorPartition = (sensorId, part) => {
    setSensors((prev) =>
      prev.map((s) => (s.id === sensorId ? { ...s, partition: part } : s))
    );
  };

  const handleToggleSensorType = (sensorId, newType) => {
    setSensors((prev) =>
      prev.map((s) => (s.id === sensorId ? { ...s, type: newType } : s))
    );
  };

  const handleToggleSensor24h = (sensorId) => {
    setSensors((prev) =>
      prev.map((s) => (s.id === sensorId ? { ...s, is24h: !s.is24h } : s))
    );
  };

  // 8. Remote Locking
  const handleToggleLockRemote = (remoteId) => {
    setRemotes((prev) =>
      prev.map((r) => (r.id === remoteId ? { ...r, isLocked: !r.isLocked } : r))
    );
  };

  const handleChangeRemotePartition = (remoteId, part) => {
    setRemotes((prev) =>
      prev.map((r) => (r.id === remoteId ? { ...r, partition: part } : r))
    );
  };

  // 9. Remote Code Save
  const handleSaveRemoteCode = (remoteName, sequence) => {
    logCommand(
      'sms',
      `SMS: #REMOTE_CODE=${remoteName}:${sequence.join('-')}*1234#`,
      `ثبت توالی کد ریموت در حافظه سخت‌افزار KDD`
    );
  };

  // 10. Contact Permissions Toggle
  const handleToggleContactPermission = (contactId, field) => {
    playSound('click');
    setContacts((prev) =>
      prev.map((c) => (c.id === contactId ? { ...c, [field]: !c[field] } : c))
    );
  };

  const handleAddContact = (newC) => {
    const nextId = contacts.length + 1;
    setContacts((prev) => [
      ...prev,
      {
        id: nextId,
        name: newC.name,
        phone: newC.phone,
        partition: newC.partition || 1,
        call: true,
        sms: true,
        powerCut: true,
        armDisarm: false,
        report: true,
        isAdmin: false,
      },
    ]);
    logCommand(
      'sms',
      `SMS: #ADD_CONTACT=${nextId}:${newC.phone}*1234#`,
      `افزودن شماره تماس جدید به لیست مجاز سیم‌کارت دزدگیر`
    );
  };

  const handleDeleteContact = (contactId) => {
    playSound('click');
    setContacts((prev) => prev.filter((c) => c.id !== contactId));
    logCommand(
      'sms',
      `SMS: #DEL_CONTACT=${contactId}*1234#`,
      `حذف مخاطب شماره ${contactId} از حافظه سخت‌افزار`
    );
  };

  // 11. Registration Complete Flow (Adds new device to TOP and goes back to My Devices!)
  const handleCompleteRegistration = () => {
    const newDev = {
      id: `kdd-custom-${Date.now()}`,
      name: regForm.name || 'کامیون جدید KDD',
      model: 'Custom Heavy Vehicle',
      serial: regForm.serial || 'KDD-FH500-0012',
      simNumber: regForm.simNumber || '09123456789',
      activeSim: regForm.activeSim || 1,
      password: regForm.password || '1234',
      isOnline: true,
      isArmed: false,
      battery: 100,
      batteryVoltage: 12.9,
      powerConnected: true,
      powerVoltage: 24.4,
      gsmSignal: 29,
      networkType: '4G LTE',
      lastSync: 'همین الان',
    };
    // Prepend to top of devices list
    setDevices((prev) => [newDev, ...prev]);
    // Reset form
    setRegForm({
      serial: 'KDD-FH500-00' + Math.floor(10 + Math.random() * 90),
      name: '',
      simNumber: '',
      activeSim: 1,
      ownerName: '',
      nationalId: '',
      ownerPhone: '',
      province: 'تهران',
      city: 'تهران',
      postalCode: '',
      technician: '',
      password: '',
      confirmPassword: '',
      biometric: true,
    });
    // Return directly to My Devices list as requested!
    setActiveScreen('my-devices');
    logCommand(
      'sms',
      `SMS: #REG_DEV=${newDev.serial}*PASS=${newDev.password}#`,
      'دستگاه جدید با موفقیت ثبت شد و در صدر لیست دستگاه‌ها قرار گرفت'
    );
  };

  // Screen Switcher Helper
  const allScreens = [
    { id: 'splash', label: 'صفحه ۰۱ — Splash / شروع اپ', num: '01' },
    { id: 'my-devices', label: 'صفحه ۰۲ — دستگاه‌های من', num: '02' },
    { id: 'register-1', label: 'صفحه ۰۳ — ثبت دستگاه (مرحله ۱)', num: '03' },
    { id: 'register-2', label: 'صفحه ۰۴ — ثبت گارانتی (مرحله ۲)', num: '04' },
    { id: 'register-3', label: 'صفحه ۰۵ — تعیین رمز (مرحله ۳)', num: '05' },
    { id: 'dashboard', label: 'صفحه ۰۶ — داشبورد / خانه', num: '06' },
    { id: 'settings', label: 'صفحه ۰۷ — منوی تنظیمات', num: '07' },
    { id: 'status', label: 'صفحه ۰۸ — وضعیت دستگاه', num: '08' },
    { id: 'outputs', label: 'صفحه ۰۹ — خروجی‌های رله', num: '09' },
    { id: 'device-settings', label: 'صفحه ۱۰ — تنظیمات سخت‌افزار', num: '10' },
    { id: 'remote-coding', label: 'صفحه ۱۱ — کدگذاری ریموت', num: '11' },
    { id: 'remotes', label: 'صفحه ۱۲ — لیست ریموت‌ها', num: '12' },
    { id: 'contacts', label: 'صفحه ۱۳ — مخاطبین و دسترسی‌ها', num: '13' },
    { id: 'sensors', label: 'صفحه ۱۴ — تنظیمات سنسورها', num: '14' },
  ];

  const hasBottomNav = ['dashboard', 'status', 'outputs', 'settings'].includes(activeScreen);

  return (
    <div className="min-h-screen bg-[#06090E] text-gray-100 flex flex-col font-['Vazirmatn',sans-serif] selection:bg-[#1F6BFF] selection:text-white" dir="rtl">
      {/* Top Global Control Toolbar */}
      <header className="bg-[#0D1117] border-b border-[#2D333B] px-4 py-2.5 flex flex-wrap items-center justify-between gap-3 sticky top-0 z-40 shadow-xl">
        {/* Brand & Title */}
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-xl bg-[#161B22] border border-[#2D333B] flex items-center justify-center p-1 shadow-[0_0_15px_rgba(31,107,255,0.3)]">
            <img src="/assets/logo_shield.png" alt="KDD" className="w-full h-full object-contain" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-sm font-black text-white">سامانه KDD Smart Security</h1>
              <span className="text-[10px] px-2 py-0.2 rounded-full bg-[#1F6BFF]/20 text-[#1F6BFF] font-mono border border-[#1F6BFF]/40">
                v1.2
              </span>
            </div>
            <p className="text-[11px] text-gray-400">سیستم حفاظتی خودروهای سنگین با کنترل پیامکی SIM800 و اینترنت</p>
          </div>
        </div>

        {/* Center: Screen Dropdown Switcher */}
        <div className="flex items-center gap-2">
          <label className="text-xs text-gray-400 hidden sm:inline">صفحه جاری:</label>
          <div className="relative">
            <select
              value={activeScreen}
              onChange={(e) => {
                playSound('click');
                setActiveScreen(e.target.value);
                if (viewMode === 'spec') setViewMode('mobile');
              }}
              className="bg-[#161B22] border border-[#2D333B] hover:border-[#1F6BFF] focus:border-[#1F6BFF] text-white text-xs font-semibold rounded-xl px-3 py-1.5 outline-none cursor-pointer pr-8"
            >
              {allScreens.map((s) => (
                <option key={s.id} value={s.id}>
                  {s.label}
                </option>
              ))}
            </select>
            <ChevronDown className="w-3.5 h-3.5 text-gray-400 absolute left-2.5 top-1/2 -translate-y-1/2 pointer-events-none" />
          </div>
        </div>

        {/* Right: View Mode Toggle */}
        <div className="flex items-center gap-2">
          <div className="flex bg-[#161B22] rounded-xl p-1 border border-[#2D333B] text-xs">
            <button
              onClick={() => {
                playSound('click');
                setViewMode('mobile');
              }}
              className={`flex items-center gap-1.5 px-3 py-1 rounded-lg transition-all ${
                viewMode === 'mobile'
                  ? 'bg-[#1F6BFF] text-white font-bold shadow-[0_0_12px_#1F6BFF]'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              <Smartphone className="w-3.5 h-3.5" />
              <span>شبیه‌ساز موبایل</span>
            </button>
            <button
              onClick={() => {
                playSound('click');
                setViewMode('spec');
              }}
              className={`flex items-center gap-1.5 px-3 py-1 rounded-lg transition-all ${
                viewMode === 'spec'
                  ? 'bg-[#1F6BFF] text-white font-bold shadow-[0_0_12px_#1F6BFF]'
                  : 'text-gray-400 hover:text-white'
              }`}
            >
              <Layers className="w-3.5 h-3.5" />
              <span>مشخصات ۱۴ صفحه</span>
            </button>
          </div>
        </div>
      </header>

      {/* Main Body */}
      <main className="flex-1 flex flex-col items-center justify-center p-2 sm:p-6 relative overflow-x-hidden">
        {viewMode === 'spec' ? (
          <DesignSpecView
            onSelectScreen={(screenKey) => {
              setActiveScreen(screenKey);
              setViewMode('mobile');
            }}
          />
        ) : (
          /* Mobile Phone Mockup (iPhone 16 Pro Style) */
          <div className="relative my-auto">
            {/* Phone Outer Chassis */}
            <div className="relative bg-[#000000] border-[6px] border-[#2C313C] rounded-[48px] shadow-[0_25px_60px_-15px_rgba(0,0,0,0.9),0_0_40px_rgba(31,107,255,0.15)] overflow-hidden transition-all duration-300 w-[375px] sm:w-[390px] h-[780px]">
              {/* Dynamic Island / Notch */}
              <div className="absolute top-2.5 left-1/2 -translate-x-1/2 w-28 h-6 bg-black rounded-full z-40 flex items-center justify-between px-2.5 border border-gray-800">
                <div className="w-2.5 h-2.5 rounded-full bg-[#1F6BFF]/40 border border-[#1F6BFF]/80 flex items-center justify-center">
                  <div className="w-1 h-1 rounded-full bg-[#1F6BFF]" />
                </div>
                <div className="flex items-center gap-1">
                  <span className={`w-1.5 h-1.5 rounded-full ${isArmed ? 'bg-emerald-400' : 'bg-blue-400'}`} />
                  <span className="text-[9px] text-gray-400 font-mono">KDD</span>
                </div>
              </div>

              {/* Status Bar (9:41, WiFi, Battery) */}
              <div className="w-full pt-3 px-6 pb-1 flex items-center justify-between text-xs text-gray-300 font-mono z-30 bg-[#0D1117]/80 backdrop-blur-md">
                <span className="font-bold text-[11px]">9:41</span>
                <div className="flex items-center gap-2 text-gray-300">
                  <Signal className="w-3.5 h-3.5 text-[#1F6BFF]" />
                  <Wifi className="w-3.5 h-3.5 text-[#1F6BFF]" />
                  <div className="flex items-center gap-1">
                    <span className="text-[10px]">{activeDevice.battery}%</span>
                    <Battery className="w-4 h-4 text-emerald-400" />
                  </div>
                </div>
              </div>

              {/* Screen Body Container */}
              <div className="w-full h-[calc(100%-70px)] bg-[#0D1117] overflow-y-auto flex flex-col relative">
                {activeScreen === 'splash' && (
                  <Screen01_Splash
                    onFinish={() => setActiveScreen('my-devices')}
                  />
                )}

                {activeScreen === 'my-devices' && (
                  <Screen02_MyDevices
                    devices={devices}
                    activeDeviceId={activeDeviceId}
                    onSelectDevice={(devId) => {
                      setActiveDeviceId(devId);
                      setActiveScreen('dashboard');
                    }}
                    onAddNew={() => setActiveScreen('register-1')}
                  />
                )}

                {activeScreen === 'register-1' && (
                  <Screen03_RegisterStep1
                    formData={regForm}
                    setFormData={setRegForm}
                    onNext={() => setActiveScreen('register-2')}
                    onBack={() => setActiveScreen('my-devices')}
                  />
                )}

                {activeScreen === 'register-2' && (
                  <Screen04_RegisterStep2
                    formData={regForm}
                    setFormData={setRegForm}
                    onNext={() => setActiveScreen('register-3')}
                    onBack={() => setActiveScreen('register-1')}
                  />
                )}

                {activeScreen === 'register-3' && (
                  <Screen05_RegisterStep3
                    formData={regForm}
                    setFormData={setRegForm}
                    onComplete={handleCompleteRegistration}
                    onBack={() => setActiveScreen('register-2')}
                  />
                )}

                {activeScreen === 'dashboard' && (
                  <Screen06_Dashboard
                    device={activeDevice}
                    isArmed={isArmed}
                    onToggleArm={handleToggleArm}
                    onOpenNotifications={() => setNotifDrawerOpen(true)}
                    unreadCount={events.length}
                  />
                )}

                {activeScreen === 'settings' && (
                  <Screen07_Settings
                    onNavigateScreen={(screenId) => setActiveScreen(screenId)}
                  />
                )}

                {activeScreen === 'status' && (
                  <Screen08_DeviceStatus
                    device={activeDevice}
                    sensors={sensors}
                    relays={relays}
                    onTriggerSensor={handleTriggerSensor}
                    isArmed={isArmed}
                  />
                )}

                {activeScreen === 'outputs' && (
                  <Screen09_Outputs
                    relays={relays}
                    onToggleRelay={handleToggleRelay}
                    onPulseRelay={handlePulseRelay}
                    onRenameRelay={handleRenameRelay}
                    onChangeRelayMode={handleChangeRelayMode}
                  />
                )}

                {activeScreen === 'device-settings' && (
                  <Screen10_DeviceSettings
                    settings={deviceSettings}
                    onUpdateSettings={setDeviceSettings}
                    onBack={() => setActiveScreen('settings')}
                    onSaveAll={() => {
                      logCommand('sms', `SMS: #SET_CONFIG=OK*1234#`, 'ذخیره کلیه تنظیمات سخت‌افزاری در EEPROM');
                    }}
                  />
                )}

                {activeScreen === 'remote-coding' && (
                  <Screen11_RemoteCoding
                    onBack={() => setActiveScreen('settings')}
                    onSaveCode={handleSaveRemoteCode}
                  />
                )}

                {activeScreen === 'remotes' && (
                  <Screen12_Remotes
                    remotes={remotes}
                    onToggleLockRemote={handleToggleLockRemote}
                    onChangePartition={handleChangeRemotePartition}
                    onBack={() => setActiveScreen('settings')}
                    onSaveAll={() => {
                      logCommand('sms', `SMS: #SAVE_REMOTES=OK*1234#`, 'همگام‌سازی ۱۰ ریموت با برد');
                    }}
                  />
                )}

                {activeScreen === 'contacts' && (
                  <Screen13_Contacts
                    contacts={contacts}
                    onTogglePermission={handleToggleContactPermission}
                    onAddContact={handleAddContact}
                    onDeleteContact={handleDeleteContact}
                    onBack={() => setActiveScreen('settings')}
                    onSaveAll={() => {
                      logCommand('sms', `SMS: #SAVE_CONTACTS=OK*1234#`, 'ارسال و ذخیره ماتریس دسترسی مخاطبین');
                    }}
                  />
                )}

                {activeScreen === 'sensors' && (
                  <Screen14_Sensors
                    sensors={sensors}
                    onChangePartition={handleChangeSensorPartition}
                    onToggleType={handleToggleSensorType}
                    onToggle24h={handleToggleSensor24h}
                    onTriggerSensor={handleTriggerSensor}
                    onBack={() => setActiveScreen('settings')}
                    onSaveAll={() => {
                      logCommand('sms', `SMS: #SAVE_SENSORS=OK*1234#`, 'ذخیره پیکربندی سنسورها و زون‌ها در ماژول');
                    }}
                  />
                )}
              </div>

              {/* Bottom Navigation (Fixed when in dashboard/status/outputs/settings) */}
              {hasBottomNav && (
                <BottomNavigation
                  activeTab={activeScreen}
                  onSelectTab={(tabId) => setActiveScreen(tabId)}
                />
              )}

              {/* Home Indicator bar */}
              <div className="w-full bg-[#0D1117] py-1.5 flex justify-center">
                <div className="w-32 h-1 bg-gray-600 rounded-full" />
              </div>
            </div>
          </div>
        )}
      </main>

      {/* Notifications Drawer */}
      <NotificationDrawer
        isOpen={notifDrawerOpen}
        onClose={() => setNotifDrawerOpen(false)}
        events={events}
      />

      {/* Bottom Live Hardware Console (SIM800 / MQTT) */}
      <HardwareTerminal
        logs={hardwareLogs}
        onClear={() => setHardwareLogs([])}
        connectionMode={connectionMode}
        setConnectionMode={setConnectionMode}
      />
    </div>
  );
}
''')

    print("Updated App.jsx created successfully!")

update_app()
