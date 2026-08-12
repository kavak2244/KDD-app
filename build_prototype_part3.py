import os

def create_screens_part3():
    # Screen 06: Dashboard / Home
    with open('/home/user/kdd-prototype/src/screens/Screen06_Dashboard.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState } from 'react';
import { Shield, ShieldAlert, ShieldCheck, Battery, Signal, Zap, Bell, Power, Lock, Unlock, Radio, AlertOctagon, RotateCw, Key } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen06_Dashboard({
  device,
  isArmed,
  onToggleArm,
  connectionMode,
  setConnectionMode,
  onOpenNotifications,
  unreadCount = 2,
  onNavigate,
  onTriggerAlarm,
  isAlarmActive,
  onResetAlarm,
}) {
  const [quickActionLoading, setQuickActionLoading] = useState(null);

  const handleArmToggle = () => {
    onToggleArm();
  };

  const handleQuickAction = (actionKey, name) => {
    playSound('relay');
    setQuickActionLoading(actionKey);
    setTimeout(() => {
      setQuickActionLoading(null);
    }, 1200);
  };

  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      {/* Top Header */}
      <div className="flex items-center justify-between mb-3 pt-1">
        {/* Notification Bell */}
        <button
          onClick={() => {
            playSound('click');
            onOpenNotifications();
          }}
          className="relative p-2 rounded-xl bg-[#161B22] border border-[#2D333B] text-gray-300 hover:text-white hover:border-[#1F6BFF] transition-all"
        >
          <Bell className="w-5 h-5" />
          {unreadCount > 0 && (
            <span className="absolute -top-1 -right-1 w-4 h-4 bg-red-500 text-white rounded-full text-[10px] font-bold flex items-center justify-center shadow-[0_0_8px_rgba(239,68,68,0.8)]">
              {unreadCount}
            </span>
          )}
        </button>

        {/* Brand & Active Device Selector */}
        <div className="text-center">
          <h2 className="text-sm font-extrabold tracking-wider text-white">KDD SMART SECURITY</h2>
          <span className="text-[11px] text-gray-400 font-mono">{device?.serial || 'KDD-FH500-0012'}</span>
        </div>

        {/* Logo Shield */}
        <div className="w-9 h-9 rounded-xl bg-[#161B22] border border-[#2D333B] flex items-center justify-center text-[#1F6BFF]">
          <Shield className="w-5 h-5" />
        </div>
      </div>

      {/* Main Content Area */}
      <div className="flex-1 space-y-3.5 overflow-y-auto pb-4">
        {/* Hero Vehicle Card with Blue Energy Ring */}
        <div className="relative rounded-2xl bg-gradient-to-b from-[#161B22] to-[#10151C] border border-[#2D333B] p-4 overflow-hidden shadow-2xl">
          {/* Subtle glow background */}
          <div className="absolute top-1/2 left-1/4 -translate-y-1/2 w-40 h-40 bg-[#1F6BFF]/20 rounded-full blur-2xl pointer-events-none" />

          <div className="flex items-center justify-between mb-3">
            {/* Connection mode pill */}
            <button
              onClick={() => {
                playSound('click');
                setConnectionMode(connectionMode === 'internet' ? 'sms' : 'internet');
              }}
              className={`flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold border transition-all ${
                connectionMode === 'internet'
                  ? 'bg-emerald-500/15 border-emerald-500/30 text-emerald-400'
                  : 'bg-amber-500/15 border-amber-500/30 text-amber-400'
              }`}
            >
              <span className={`w-2 h-2 rounded-full ${connectionMode === 'internet' ? 'bg-emerald-400 animate-pulse' : 'bg-amber-400'}`} />
              <span>{connectionMode === 'internet' ? 'سیستم آنلاین است' : 'حالت پیامکی GSM'}</span>
            </button>

            {/* Vehicle Name */}
            <div className="text-right">
              <h3 className="text-lg font-black text-white">{device?.name?.split('—')[0] || 'FH500'}</h3>
              <p className="text-[11px] text-gray-400">{device?.model || 'Volvo FH500'}</p>
            </div>
          </div>

          {/* Vehicle Visual with Energy Ring */}
          <div className="flex items-center justify-center my-2 relative">
            {/* Glowing Ring underneath */}
            <div className={`w-44 h-16 rounded-full border border-[#1F6BFF]/50 absolute bottom-1 shadow-[0_0_25px_#1F6BFF] ${
              isAlarmActive ? 'border-red-500 shadow-[0_0_30px_#EF4444]' : isArmed ? 'border-[#1F6BFF] kdd-energy-ring' : 'border-gray-600'
            }`} />

            <img
              src="/screens/06_داشبورد___خانه.jpg"
              alt="Volvo FH500 Heavy Truck"
              className="w-40 h-28 object-contain object-top rounded-xl mix-blend-lighten z-10 drop-shadow-[0_10px_20px_rgba(0,0,0,0.8)]"
              onError={(e) => {
                // Fallback SVG if image not found
                e.target.style.display = 'none';
              }}
            />
          </div>

          {/* Quick Metrics under hero */}
          <div className="grid grid-cols-2 gap-2.5 mt-3 pt-3 border-t border-[#2D333B]/60">
            <div className="p-2.5 rounded-xl bg-[#0D1117]/80 border border-[#2D333B] flex items-center justify-between">
              <div className="w-8 h-8 rounded-lg bg-blue-500/10 text-[#1F6BFF] flex items-center justify-center">
                <Signal className="w-4 h-4" />
              </div>
              <div className="text-right">
                <span className="text-[10px] text-gray-400 block">سیگنال GSM</span>
                <span className="text-xs font-bold text-white">عالی (4G)</span>
              </div>
            </div>

            <div className="p-2.5 rounded-xl bg-[#0D1117]/80 border border-[#2D333B] flex items-center justify-between">
              <div className="w-8 h-8 rounded-lg bg-emerald-500/10 text-emerald-400 flex items-center justify-center">
                <Battery className="w-4 h-4" />
              </div>
              <div className="text-right">
                <span className="text-[10px] text-gray-400 block">باتری دستگاه</span>
                <span className="text-xs font-bold text-white font-mono">{device?.battery || 98}% (12.8V)</span>
              </div>
            </div>
          </div>
        </div>

        {/* Protection Status Hero Card (ARM / DISARM) */}
        <div className={`rounded-2xl border p-4.5 transition-all relative overflow-hidden ${
          isAlarmActive
            ? 'bg-gradient-to-r from-red-950/40 to-[#161B22] border-red-500 kdd-alarm-active shadow-[0_0_30px_rgba(239,68,68,0.4)]'
            : isArmed
            ? 'bg-gradient-to-r from-blue-950/30 to-[#161B22] border-[#1F6BFF] shadow-[0_0_25px_rgba(31,107,255,0.25)]'
            : 'bg-[#161B22] border-[#2D333B]'
        }`}>
          <div className="flex items-center justify-between">
            {/* Toggle Switch */}
            <div className="flex flex-col items-center gap-2">
              <button
                onClick={handleArmToggle}
                className={`w-16 h-8 rounded-full p-1 transition-all duration-300 relative shadow-inner ${
                  isArmed ? 'bg-[#1F6BFF] shadow-[0_0_15px_#1F6BFF]' : 'bg-[#2D333B]'
                }`}
              >
                <div className={`w-6 h-6 rounded-full bg-white transition-transform duration-300 flex items-center justify-center ${
                  isArmed ? '-translate-x-8' : 'translate-x-0'
                }`}>
                  {isArmed ? <Lock className="w-3.5 h-3.5 text-[#1F6BFF]" /> : <Unlock className="w-3.5 h-3.5 text-gray-700" />}
                </div>
              </button>
              <span className="text-[10px] text-gray-400">
                {isArmed ? 'لمس برای غیرفعال' : 'لمس برای فعال‌سازی'}
              </span>
            </div>

            {/* Status Text & Shield Indicator */}
            <div className="flex items-center gap-3 text-right">
              <div>
                <span className="text-xs text-gray-400 block mb-0.5">سیستم حفاظتی خودرو</span>
                <h3 className={`text-xl font-black ${
                  isAlarmActive ? 'text-red-400 animate-bounce' : isArmed ? 'text-emerald-400' : 'text-blue-400'
                }`}>
                  {isAlarmActive ? 'آلارم و هشدار خطر!' : isArmed ? 'فعال (مسلح)' : 'غیرفعال (آماده)'}
                </h3>
                <p className="text-[11px] text-gray-400 mt-0.5">
                  {isAlarmActive ? 'تحریک سنسور شناسایی شد!' : isArmed ? 'تمام سنسورها و زون‌ها تحت حفاظت' : 'حفاظت غیرفعال است'}
                </p>
              </div>

              {/* Glowing Shield Icon */}
              <div className={`relative w-14 h-14 rounded-2xl flex items-center justify-center border transition-all ${
                isAlarmActive
                  ? 'bg-red-500/20 border-red-500 text-red-400 shadow-[0_0_20px_rgba(239,68,68,0.6)]'
                  : isArmed
                  ? 'bg-[#1F6BFF]/20 border-[#1F6BFF] text-[#1F6BFF] shadow-[0_0_20px_rgba(31,107,255,0.4)]'
                  : 'bg-[#0D1117] border-[#2D333B] text-gray-400'
              }`}>
                {isAlarmActive ? <ShieldAlert className="w-8 h-8" /> : isArmed ? <ShieldCheck className="w-8 h-8" /> : <Shield className="w-8 h-8" />}
              </div>
            </div>
          </div>

          {/* Alarm Reset Button if Triggered */}
          {isAlarmActive && (
            <div className="mt-3 pt-3 border-t border-red-500/30 flex items-center justify-between">
              <button
                onClick={() => {
                  playSound('disarm');
                  onResetAlarm();
                }}
                className="w-full py-2 rounded-xl bg-red-600 hover:bg-red-500 text-white font-bold text-xs shadow-[0_0_15px_rgba(239,68,68,0.6)] transition-all flex items-center justify-center gap-2"
              >
                <Power className="w-4 h-4" />
                <span>خاموش کردن آژیر و قطع وضعیت اضطراری</span>
              </button>
            </div>
          )}
        </div>

        {/* Quick Actions Grid */}
        <div>
          <div className="flex items-center justify-between mb-2">
            <h4 className="text-xs font-bold text-gray-300">فرمان‌های سریع راننده</h4>
            <span className="text-[10px] text-gray-500">ارسال لحظه‌ای فرمان</span>
          </div>

          <div className="grid grid-cols-4 gap-2">
            {/* SOS Panic */}
            <button
              onClick={() => {
                if (isAlarmActive) {
                  onResetAlarm();
                } else {
                  onTriggerAlarm();
                }
              }}
              className={`p-2.5 rounded-xl border flex flex-col items-center justify-center gap-1.5 transition-all ${
                isAlarmActive
                  ? 'bg-red-600 text-white border-red-500 shadow-[0_0_15px_rgba(239,68,68,0.5)]'
                  : 'bg-red-500/10 hover:bg-red-500/20 text-red-400 border-red-500/30'
              }`}
            >
              <AlertOctagon className="w-5 h-5" />
              <span className="text-[10px] font-bold">آژیر SOS</span>
            </button>

            {/* Unlock Doors */}
            <button
              onClick={() => handleQuickAction('unlock', 'بازکردن درب')}
              className={`p-2.5 rounded-xl bg-[#161B22] hover:bg-[#2D333B] text-gray-300 hover:text-white border border-[#2D333B] flex flex-col items-center justify-center gap-1.5 transition-all ${
                quickActionLoading === 'unlock' ? 'border-[#1F6BFF] text-[#1F6BFF]' : ''
              }`}
            >
              <Unlock className={`w-5 h-5 ${quickActionLoading === 'unlock' ? 'animate-bounce' : ''}`} />
              <span className="text-[10px] font-semibold">دربازکن</span>
            </button>

            {/* Flasher */}
            <button
              onClick={() => handleQuickAction('flash', 'فلاشر')}
              className={`p-2.5 rounded-xl bg-[#161B22] hover:bg-[#2D333B] text-gray-300 hover:text-white border border-[#2D333B] flex flex-col items-center justify-center gap-1.5 transition-all ${
                quickActionLoading === 'flash' ? 'border-amber-400 text-amber-400' : ''
              }`}
            >
              <Zap className={`w-5 h-5 ${quickActionLoading === 'flash' ? 'animate-pulse text-amber-400' : ''}`} />
              <span className="text-[10px] font-semibold">فلاشر</span>
            </button>

            {/* Status Query */}
            <button
              onClick={() => {
                handleQuickAction('query', 'استعلام');
                onNavigate('status');
              }}
              className="p-2.5 rounded-xl bg-[#161B22] hover:bg-[#2D333B] text-gray-300 hover:text-white border border-[#2D333B] flex flex-col items-center justify-center gap-1.5 transition-all"
            >
              <RotateCw className="w-5 h-5" />
              <span className="text-[10px] font-semibold">وضعیت اجزا</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
''')

    # Screen 07: Settings Hub
    with open('/home/user/kdd-prototype/src/screens/Screen07_Settings.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React from 'react';
import { ChevronLeft, Radio, Users, Cpu, Key, Lock, Settings as SettingsIcon, Wifi, CreditCard, RefreshCw, ShieldCheck } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen07_Settings({ onNavigateScreen }) {
  const menuItems = [
    { id: 14, label: 'سنسورها (پارتیشن، NO/NC، حالت ۲۴ساعته)', icon: Radio, screen: 'sensors' },
    { id: 13, label: 'مخاطبین (شماره‌ها و سطح دسترسی‌ها)', icon: Users, screen: 'contacts' },
    { id: 12, label: 'ریموت‌ها (مدیریت و تعیین پارتیشن)', icon: Cpu, screen: 'remotes' },
    { id: 11, label: 'کدگذاری ریموت‌ها (ثبت توالی کلیدها)', icon: Key, screen: 'remote-coding' },
    { id: 10, label: 'تنظیمات دستگاه (سخت‌افزار، آژیر، پیامک)', icon: SettingsIcon, screen: 'device-settings' },
    { id: 5, label: 'مدیریت رمز عبور و ورود بیومتریک', icon: Lock, screen: 'register-3' },
    { id: 8, label: 'تنظیم اینترنت، سرور و پروتکل MQTT', icon: Wifi, screen: 'status' },
    { id: 3, label: 'تنظیم سیم‌کارت و استعلام شارژ', icon: CreditCard, screen: 'register-1' },
    { id: 6, label: 'همگام‌سازی اطلاعات با حافظه برد SIM800', icon: RefreshCw, screen: 'dashboard' },
    { id: 4, label: 'اطلاعات گارانتی و پشتیبانی ۲۴ ساعته', icon: ShieldCheck, screen: 'register-2' },
  ];

  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      <div className="mb-4 pt-1">
        <h2 className="text-xl font-bold text-white mb-1">تنظیمات سامانه KDD</h2>
        <p className="text-xs text-gray-400">پیکربندی سنسورها، ریموت‌ها، مخاطبین و سخت‌افزار</p>
      </div>

      <div className="flex-1 space-y-2 overflow-y-auto pb-4">
        {menuItems.map((item) => {
          const Icon = item.icon;
          return (
            <div
              key={item.id}
              onClick={() => {
                playSound('click');
                onNavigateScreen(item.screen);
              }}
              className="p-3.5 rounded-2xl bg-[#161B22] border border-[#2D333B] hover:border-[#1F6BFF] hover:bg-[#1a2332] transition-all flex items-center justify-between cursor-pointer group"
            >
              <ChevronLeft className="w-4 h-4 text-gray-400 group-hover:-translate-x-1 group-hover:text-[#1F6BFF] transition-all" />
              
              <div className="flex items-center gap-3 text-right">
                <span className="text-xs font-semibold text-gray-200 group-hover:text-white">
                  {item.label}
                </span>
                <div className="w-9 h-9 rounded-xl bg-[#0D1117] border border-[#2D333B] text-[#1F6BFF] flex items-center justify-center group-hover:border-[#1F6BFF]/50 group-hover:shadow-[0_0_12px_rgba(31,107,255,0.3)] transition-all">
                  <Icon className="w-4 h-4" />
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
''')

    # Screen 08: Device Status
    with open('/home/user/kdd-prototype/src/screens/Screen08_DeviceStatus.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React from 'react';
import { Shield, ShieldCheck, Battery, Zap, Signal, Wifi, Radio, Power, RefreshCw, CheckCircle2, AlertTriangle } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen08_DeviceStatus({ device, sensors, relays, onTriggerSensor, isArmed }) {
  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      <div className="mb-4 pt-1">
        <h2 className="text-xl font-bold text-white mb-1">وضعیت کلی دستگاه</h2>
        <p className="text-xs text-gray-400">تله‌متری زنده سنسورها، ولتاژ باتری و شبکه ارتباطی</p>
      </div>

      <div className="flex-1 space-y-4 overflow-y-auto pb-4">
        {/* Status Header Card */}
        <div className="p-4 rounded-2xl bg-gradient-to-b from-[#161B22] to-[#12171F] border border-[#2D333B] flex items-center justify-between">
          <div className="w-12 h-12 rounded-2xl bg-[#1F6BFF]/15 border border-[#1F6BFF]/40 text-[#1F6BFF] flex items-center justify-center shadow-[0_0_20px_rgba(31,107,255,0.3)]">
            <ShieldCheck className="w-7 h-7" />
          </div>
          <div className="text-right">
            <div className="flex items-center justify-end gap-2 mb-0.5">
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
              <h3 className="text-base font-bold text-emerald-400">سیستم متصل و آنلاین است</h3>
            </div>
            <p className="text-xs text-gray-400">وضعیت اجزای سخت‌افزاری و برقراری ارتباط</p>
          </div>
        </div>

        {/* Telemetry Key/Value Rows */}
        <div className="rounded-2xl bg-[#161B22] border border-[#2D333B] divide-y divide-[#2D333B]/60 overflow-hidden">
          <div className="p-3 flex items-center justify-between text-xs">
            <span className="font-semibold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded">متصل (Ready)</span>
            <div className="flex items-center gap-2 text-gray-300">
              <span>وضعیت ماژول SIM800:</span>
              <Radio className="w-4 h-4 text-[#1F6BFF]" />
            </div>
          </div>

          <div className="p-3 flex items-center justify-between text-xs">
            <span className="font-mono font-semibold text-white">98% (12.8V DC)</span>
            <div className="flex items-center gap-2 text-gray-300">
              <span>باتری پشتیبان:</span>
              <Battery className="w-4 h-4 text-emerald-400" />
            </div>
          </div>

          <div className="p-3 flex items-center justify-between text-xs">
            <span className="font-mono font-semibold text-emerald-400">وصل (24.2V دینام)</span>
            <div className="flex items-center gap-2 text-gray-300">
              <span>برق ورودی خودرو:</span>
              <Zap className="w-4 h-4 text-amber-400" />
            </div>
          </div>

          <div className="p-3 flex items-center justify-between text-xs">
            <span className="font-semibold text-white">عالی (28/31 RSSI)</span>
            <div className="flex items-center gap-2 text-gray-300">
              <span>قدرت آنتن GSM:</span>
              <Signal className="w-4 h-4 text-blue-400" />
            </div>
          </div>

          <div className="p-3 flex items-center justify-between text-xs">
            <span className="font-semibold text-emerald-400">آنلاین (GPRS / 4G)</span>
            <div className="flex items-center gap-2 text-gray-300">
              <span>شبکه اینترنت:</span>
              <Wifi className="w-4 h-4 text-[#1F6BFF]" />
            </div>
          </div>
        </div>

        {/* Live Sensors Grid (8 Sensors) */}
        <div>
          <div className="flex items-center justify-between mb-2">
            <span className="text-[11px] text-gray-500 font-mono">لمس هر سنسور = تست شبیه‌سازی تحریک</span>
            <h4 className="text-xs font-bold text-gray-300">وضعیت سنسورها (۸ زون)</h4>
          </div>

          <div className="grid grid-cols-2 gap-2">
            {sensors.map((s) => (
              <button
                key={s.id}
                onClick={() => {
                  playSound('click');
                  onTriggerSensor(s.id);
                }}
                className={`p-2.5 rounded-xl border flex items-center justify-between transition-all ${
                  s.isTriggered
                    ? 'bg-red-500/20 border-red-500 text-red-300 shadow-[0_0_15px_rgba(239,68,68,0.4)]'
                    : 'bg-[#161B22] border-[#2D333B] text-gray-300 hover:border-gray-600'
                }`}
              >
                <span className={`text-[10px] px-1.5 py-0.5 rounded font-bold ${
                  s.isTriggered ? 'bg-red-500 text-white' : 'bg-emerald-500/20 text-emerald-400'
                }`}>
                  {s.isTriggered ? 'تحریک شد!' : 'فعال'}
                </span>

                <span className="text-xs font-medium truncate max-w-[100px]">
                  سنسور {s.id}
                </span>
              </button>
            ))}
          </div>
        </div>

        {/* Live Outputs Grid (8 Relays) */}
        <div>
          <div className="flex items-center justify-between mb-2">
            <span className="text-[11px] text-gray-500 font-mono">وضعیت قطع و وصل رله‌ها</span>
            <h4 className="text-xs font-bold text-gray-300">وضعیت خروجی‌ها (۸ رله)</h4>
          </div>

          <div className="grid grid-cols-2 gap-2">
            {relays.map((r) => (
              <div
                key={r.id}
                className="p-2.5 rounded-xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between text-xs"
              >
                <span className={`text-[10px] px-1.5 py-0.5 rounded font-bold ${
                  r.state ? 'bg-[#1F6BFF]/20 text-[#1F6BFF]' : 'bg-gray-800 text-gray-400'
                }`}>
                  {r.state ? 'روشن' : 'خاموش'}
                </span>
                <span className="text-gray-300 truncate max-w-[100px]">
                  خروجی {r.id}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
''')

    # Screen 09: Outputs / Relays
    with open('/home/user/kdd-prototype/src/screens/Screen09_Outputs.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState } from 'react';
import { Zap, Power, Clock, Edit2, ShieldAlert, Check } from 'lucide-react';
import { playSound } from '../utils/audio';
import ConfirmModal from '../components/ConfirmModal';

export default function Screen09_Outputs({ relays, onToggleRelay, onPulseRelay, onRenameRelay, onChangeRelayMode }) {
  const [editingRelay, setEditingRelay] = useState(null);
  const [tempName, setTempName] = useState('');
  const [confirmModalData, setConfirmModalData] = useState(null);

  const handleToggleClick = (relay) => {
    if (relay.isCritical && !relay.state) {
      setConfirmModalData({
        title: `فعال‌سازی ${relay.name}`,
        message: 'این خروجی دارای اهمیت امنیتی بالا است (قطع‌کن استارت/سوخت یا پمپ). آیا از ارسال فرمان مطمئن هستید؟',
        isDangerous: true,
        action: () => onToggleRelay(relay.id),
      });
    } else {
      playSound('relay');
      onToggleRelay(relay.id);
    }
  };

  const handlePulseClick = (relay) => {
    playSound('relay');
    onPulseRelay(relay.id);
  };

  const handleSaveRename = () => {
    if (editingRelay && tempName.trim()) {
      onRenameRelay(editingRelay.id, tempName.trim());
      setEditingRelay(null);
    }
  };

  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      {/* Top Banner */}
      <div className="p-3.5 rounded-2xl bg-gradient-to-b from-[#161B22] to-[#12171F] border border-[#2D333B] flex items-center justify-between mb-4">
        <div className="w-10 h-10 rounded-xl bg-[#1F6BFF]/15 border border-[#1F6BFF]/30 text-[#1F6BFF] flex items-center justify-center">
          <Zap className="w-5 h-5" />
        </div>
        <div className="text-right">
          <h2 className="text-base font-bold text-white mb-0.5">مدیریت خروجی‌های رله</h2>
          <p className="text-xs text-gray-400">کنترل، تغییر نام و زمان‌بندی ۸ رله سخت‌افزاری</p>
        </div>
      </div>

      {/* Relays List */}
      <div className="flex-1 space-y-2.5 overflow-y-auto pb-4">
        {relays.map((relay) => (
          <div
            key={relay.id}
            className={`p-3 rounded-2xl border transition-all ${
              relay.state
                ? 'bg-[#161B22] border-[#1F6BFF] shadow-[0_0_15px_rgba(31,107,255,0.2)]'
                : 'bg-[#161B22] border-[#2D333B]'
            }`}
          >
            {/* Header: Name + Edit */}
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center gap-1.5">
                <button
                  onClick={() => {
                    setEditingRelay(relay);
                    setTempName(relay.name);
                  }}
                  className="p-1 rounded-lg text-gray-400 hover:text-white hover:bg-[#2D333B]"
                  title="تغییر نام خروجی"
                >
                  <Edit2 className="w-3.5 h-3.5" />
                </button>
                <select
                  value={relay.mode}
                  onChange={(e) => onChangeRelayMode(relay.id, e.target.value)}
                  className="bg-[#0D1117] border border-[#2D333B] rounded-lg px-2 py-0.5 text-[11px] text-gray-300 outline-none"
                >
                  <option value="مستقل">مستقل</option>
                  <option value="پارتیشن ۱">پارتیشن ۱</option>
                  <option value="پارتیشن ۲">پارتیشن ۲</option>
                  <option value="اتوماتیک">اتوماتیک</option>
                </select>
              </div>

              <div className="flex items-center gap-2">
                <span className="text-xs font-bold text-white">خروجی {relay.id} — {relay.name}</span>
                {relay.isCritical && (
                  <span className="w-2 h-2 rounded-full bg-red-500 shadow-[0_0_6px_#EF4444]" title="خروجی حساس" />
                )}
              </div>
            </div>

            {/* Action Segmented Controls */}
            <div className="grid grid-cols-3 gap-2">
              <button
                onClick={() => handleToggleClick(relay)}
                className={`py-1.5 rounded-xl text-xs font-semibold flex items-center justify-center gap-1 transition-all ${
                  !relay.state
                    ? 'bg-gray-700/60 text-white border border-gray-500'
                    : 'bg-[#0D1117] text-gray-400 hover:text-white border border-[#2D333B]'
                }`}
              >
                <Power className="w-3.5 h-3.5" />
                <span>خاموش</span>
              </button>

              <button
                onClick={() => handleToggleClick(relay)}
                className={`py-1.5 rounded-xl text-xs font-semibold flex items-center justify-center gap-1 transition-all ${
                  relay.state
                    ? 'bg-[#1F6BFF] text-white shadow-[0_0_12px_#1F6BFF]'
                    : 'bg-[#0D1117] text-gray-400 hover:text-white border border-[#2D333B]'
                }`}
              >
                <Zap className="w-3.5 h-3.5" />
                <span>روشن</span>
              </button>

              <button
                onClick={() => handlePulseClick(relay)}
                className="py-1.5 rounded-xl bg-[#0D1117] text-gray-400 hover:text-[#1F6BFF] hover:border-[#1F6BFF] border border-[#2D333B] text-xs font-semibold flex items-center justify-center gap-1 transition-all"
              >
                <Clock className="w-3.5 h-3.5" />
                <span>لحظه‌ای</span>
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* Rename Modal */}
      {editingRelay && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-sm">
          <div className="w-full max-w-xs bg-[#161B22] border border-[#2D333B] rounded-2xl p-4 text-right">
            <h3 className="text-sm font-bold text-white mb-2">تغییر نام خروجی {editingRelay.id}</h3>
            <input
              type="text"
              value={tempName}
              onChange={(e) => setTempName(e.target.value)}
              className="w-full bg-[#0D1117] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3 py-2 text-xs text-white outline-none mb-4"
              placeholder="نام جدید رله..."
            />
            <div className="flex gap-2">
              <button
                onClick={() => setEditingRelay(null)}
                className="flex-1 py-2 rounded-xl bg-[#0D1117] border border-[#2D333B] text-xs text-gray-300"
              >
                انصراف
              </button>
              <button
                onClick={handleSaveRename}
                className="flex-1 py-2 rounded-xl bg-[#1F6BFF] text-xs text-white font-bold"
              >
                ذخیره نام
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Confirm Modal */}
      <ConfirmModal
        isOpen={!!confirmModalData}
        onClose={() => setConfirmModalData(null)}
        onConfirm={confirmModalData?.action || (() => {})}
        title={confirmModalData?.title || ''}
        message={confirmModalData?.message || ''}
        isDangerous={confirmModalData?.isDangerous}
      />
    </div>
  );
}
''')

    # Screen 10: Device Settings
    with open('/home/user/kdd-prototype/src/screens/Screen10_DeviceSettings.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState } from 'react';
import { Save, ArrowRight, Zap, Battery, Globe, PhoneCall, Radio, Mic, Volume2, Clock, ShieldAlert, Trash2, RotateCcw, Check } from 'lucide-react';
import { playSound } from '../utils/audio';
import ConfirmModal from '../components/ConfirmModal';

export default function Screen10_DeviceSettings({ settings, onUpdateSettings, onBack, onSaveAll }) {
  const [localSettings, setLocalSettings] = useState(settings);
  const [confirmModalData, setConfirmModalData] = useState(null);
  const [sirenModalOpen, setSirenModalOpen] = useState(false);
  const [tempDuration, setTempDuration] = useState(localSettings.sirenDurationMinutes || 1);

  const toggleSetting = (key) => {
    playSound('click');
    setLocalSettings(prev => ({ ...prev, [key]: !prev[key] }));
  };

  const handleActionClick = (title, message) => {
    playSound('arm');
    setConfirmModalData({
      title,
      message,
      action: () => {},
    });
  };

  const handleDeleteDevice = () => {
    setConfirmModalData({
      title: 'حذف دستگاه از حساب کاربری',
      message: 'آیا از حذف این دزدگیر مطمئن هستید؟ با این کار تمام دسترسی‌ها و تاریخچه‌ها پاک خواهند شد.',
      isDangerous: true,
      action: () => {
        playSound('alarm');
        onBack();
      },
    });
  };

  const handleFactoryReset = () => {
    setConfirmModalData({
      title: 'بازگردانی به تنظیمات کارخانه (Factory Reset)',
      message: 'تمام تنظیمات سنسورها، ریموت‌ها و کدهای ذخیره شده در EEPROM ماژول به حالت پیش‌فرض برمی‌گردد.',
      isDangerous: true,
      action: () => {
        playSound('alarm');
      },
    });
  };

  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      {/* Header */}
      <div className="flex items-center justify-between mb-4 pt-1">
        <button
          onClick={() => {
            playSound('click');
            onBack();
          }}
          className="p-2 rounded-xl bg-[#161B22] border border-[#2D333B] text-gray-300 hover:text-white"
        >
          <ArrowRight className="w-4 h-4" />
        </button>

        <h2 className="text-base font-bold text-white">تنظیمات سخت‌افزاری دستگاه</h2>

        <button
          onClick={() => {
            playSound('arm');
            onUpdateSettings(localSettings);
            onSaveAll();
          }}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-[#1F6BFF] hover:bg-[#1A5BDB] text-white text-xs font-bold shadow-[0_0_12px_#1F6BFF]"
        >
          <Save className="w-3.5 h-3.5" />
          <span>ذخیره</span>
        </button>
      </div>

      {/* Settings Rows */}
      <div className="flex-1 space-y-2.5 overflow-y-auto pb-4">
        {/* SMS on Power Cut */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <div className="flex gap-1.5">
            <button
              onClick={() => toggleSetting('powerCutSms')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                localSettings.powerCutSms ? 'bg-[#1F6BFF] text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              فعال
            </button>
            <button
              onClick={() => toggleSetting('powerCutSms')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                !localSettings.powerCutSms ? 'bg-gray-700 text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              غیرفعال
            </button>
          </div>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">پیامک قطع برق ۲۴V</span>
            <Zap className="w-4 h-4 text-[#1F6BFF]" />
          </div>
        </div>

        {/* SMS Battery Test */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <div className="flex gap-1.5">
            <button
              onClick={() => toggleSetting('batteryTestSms')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                localSettings.batteryTestSms ? 'bg-[#1F6BFF] text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              فعال
            </button>
            <button
              onClick={() => toggleSetting('batteryTestSms')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                !localSettings.batteryTestSms ? 'bg-gray-700 text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              غیرفعال
            </button>
          </div>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">پیامک تست دوره‌ای باتری</span>
            <Battery className="w-4 h-4 text-emerald-400" />
          </div>
        </div>

        {/* Device Language */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <div className="flex gap-1.5">
            <button
              onClick={() => setLocalSettings({ ...localSettings, language: 'فارسی' })}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                localSettings.language === 'فارسی' ? 'bg-[#1F6BFF] text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              فارسی
            </button>
            <button
              onClick={() => setLocalSettings({ ...localSettings, language: 'انگلیسی' })}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                localSettings.language === 'انگلیسی' ? 'bg-[#1F6BFF] text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              English
            </button>
          </div>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">زبان دستگاه و پیامک‌ها</span>
            <Globe className="w-4 h-4 text-[#1F6BFF]" />
          </div>
        </div>

        {/* Call on Power Cut */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <div className="flex gap-1.5">
            <button
              onClick={() => toggleSetting('callOnPowerCut')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                localSettings.callOnPowerCut ? 'bg-[#1F6BFF] text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              فعال
            </button>
            <button
              onClick={() => toggleSetting('callOnPowerCut')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                !localSettings.callOnPowerCut ? 'bg-gray-700 text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              غیرفعال
            </button>
          </div>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">تماس خودکار در قطعی برق</span>
            <PhoneCall className="w-4 h-4 text-blue-400" />
          </div>
        </div>

        {/* Remote Semi-arm Mode */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <div className="flex gap-1.5">
            <button
              onClick={() => toggleSetting('remoteSemiArm')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                localSettings.remoteSemiArm ? 'bg-[#1F6BFF] text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              فعال
            </button>
            <button
              onClick={() => toggleSetting('remoteSemiArm')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                !localSettings.remoteSemiArm ? 'bg-gray-700 text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              غیرفعال
            </button>
          </div>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">حالت نیمه‌فعال ریموت</span>
            <Radio className="w-4 h-4 text-[#1F6BFF]" />
          </div>
        </div>

        {/* Remote learn trigger */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <button
            onClick={() => handleActionClick('افزودن ریموت از راه دور', 'فرمان آماده‌سازی لرن ریموت به سخت‌افزار ارسال شد. دکمه ریموت را فشار دهید.')}
            className="px-3.5 py-1.5 rounded-xl bg-[#0D1117] border border-[#1F6BFF]/40 text-[#1F6BFF] hover:bg-[#1F6BFF] hover:text-white text-xs font-bold transition-all"
          >
            اعمال
          </button>
          <span className="text-xs font-semibold text-gray-200">اضافه کردن ریموت از راه دور</span>
        </div>

        {/* Wireless sensor learn trigger */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <button
            onClick={() => handleActionClick('افزودن سنسور بی‌سیم', 'فرمان آماده‌سازی شناسه سنسور بی‌سیم به ماژول ارسال شد.')}
            className="px-3.5 py-1.5 rounded-xl bg-[#0D1117] border border-[#1F6BFF]/40 text-[#1F6BFF] hover:bg-[#1F6BFF] hover:text-white text-xs font-bold transition-all"
          >
            اعمال
          </button>
          <span className="text-xs font-semibold text-gray-200">اضافه کردن سنسور بی‌سیم از راه دور</span>
        </div>

        {/* Voice Record */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <button
            onClick={() => handleActionClick('ضبط صدا در دستگاه', 'دستگاه آماده ضبط صدای هشدار به مدت ۲۰ ثانیه می‌باشد.')}
            className="px-3.5 py-1.5 rounded-xl bg-[#0D1117] border border-[#1F6BFF]/40 text-[#1F6BFF] hover:bg-[#1F6BFF] hover:text-white text-xs font-bold transition-all"
          >
            اعمال
          </button>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">ضبط صدا روی حافظه برد</span>
            <Mic className="w-4 h-4 text-rose-400" />
          </div>
        </div>

        {/* Speaker Melody */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <select
            value={localSettings.speakerMelody}
            onChange={(e) => setLocalSettings({ ...localSettings, speakerMelody: e.target.value })}
            className="bg-[#0D1117] border border-[#2D333B] rounded-xl px-3 py-1.5 text-xs text-white outline-none"
          >
            <option value="ملودی ۱">ملودی ۱ (کلاسیک)</option>
            <option value="ملودی ۲">ملودی ۲ (مدرن)</option>
            <option value="ملودی ۳">ملودی ۳ (صنعتی)</option>
            <option value="ملودی ۴">ملودی ۴ (پالس سریع)</option>
          </select>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">ملودی اسپیکر و آژیر</span>
            <Volume2 className="w-4 h-4 text-amber-400" />
          </div>
        </div>

        {/* Siren Duration */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <button
            onClick={() => setSirenModalOpen(true)}
            className="px-3 py-1.5 rounded-xl bg-[#0D1117] border border-[#2D333B] text-xs text-gray-300 hover:text-white flex items-center gap-1.5"
          >
            <span>ویرایش ({localSettings.sirenDurationMinutes} دقیقه)</span>
          </button>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">مدت زمان فعال ماندن آژیر</span>
            <Clock className="w-4 h-4 text-[#1F6BFF]" />
          </div>
        </div>

        {/* Alarm Mode */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <select
            value={localSettings.alarmMode}
            onChange={(e) => setLocalSettings({ ...localSettings, alarmMode: e.target.value })}
            className="bg-[#0D1117] border border-[#2D333B] rounded-xl px-2 py-1.5 text-xs text-white outline-none max-w-[190px]"
          >
            <option value="ابتدا تماس سپس پیامک با تکرار">تماس ➔ پیامک با تکرار</option>
            <option value="پیامک و تماس همزمان">پیامک و تماس همزمان</option>
            <option value="فقط پیامک اضطراری">فقط پیامک اضطراری</option>
          </select>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">مُد آلارم اضطراری</span>
            <ShieldAlert className="w-4 h-4 text-red-400" />
          </div>
        </div>

        {/* Delete Device Button */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-red-500/30 flex items-center justify-between">
          <button
            onClick={handleDeleteDevice}
            className="px-3.5 py-1.5 rounded-xl bg-red-600/20 text-red-400 hover:bg-red-600 hover:text-white border border-red-500/40 text-xs font-bold transition-all"
          >
            اعمال حذف
          </button>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-red-400">حذف دستگاه از نرم‌افزار</span>
            <Trash2 className="w-4 h-4 text-red-400" />
          </div>
        </div>

        {/* Factory Reset */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <button
            onClick={handleFactoryReset}
            className="px-3.5 py-1.5 rounded-xl bg-[#0D1117] border border-[#2D333B] text-gray-400 hover:text-amber-400 text-xs font-bold transition-all"
          >
            بازگردانی
          </button>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-300">بازگردانی به تنظیمات اولیه کارخانه</span>
            <RotateCcw className="w-4 h-4 text-gray-400" />
          </div>
        </div>
      </div>

      {/* Siren duration modal */}
      {sirenModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm">
          <div className="w-full max-w-xs bg-[#161B22] border border-[#2D333B] rounded-2xl p-4 text-right">
            <h3 className="text-sm font-bold text-white mb-2">تعیین مدت زمان آژیر</h3>
            <p className="text-xs text-gray-400 mb-4">مدت فعال ماندن خروجی آژیر پس از هر بار تحریک سنسورها:</p>
            <div className="flex items-center justify-center gap-3 mb-5">
              <span className="text-2xl font-black text-[#1F6BFF] font-mono">{tempDuration}</span>
              <span className="text-sm text-gray-300">دقیقه</span>
            </div>
            <input
              type="range"
              min="1"
              max="10"
              value={tempDuration}
              onChange={(e) => setTempDuration(Number(e.target.value))}
              className="w-full mb-5 accent-[#1F6BFF]"
            />
            <div className="flex gap-2">
              <button
                onClick={() => setSirenModalOpen(false)}
                className="flex-1 py-2 rounded-xl bg-[#0D1117] border border-[#2D333B] text-xs text-gray-300"
              >
                انصراف
              </button>
              <button
                onClick={() => {
                  setLocalSettings({ ...localSettings, sirenDurationMinutes: tempDuration });
                  setSirenModalOpen(false);
                }}
                className="flex-1 py-2 rounded-xl bg-[#1F6BFF] text-xs text-white font-bold"
              >
                تأیید
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Confirm Modal */}
      <ConfirmModal
        isOpen={!!confirmModalData}
        onClose={() => setConfirmModalData(null)}
        onConfirm={confirmModalData?.action || (() => {})}
        title={confirmModalData?.title || ''}
        message={confirmModalData?.message || ''}
        isDangerous={confirmModalData?.isDangerous}
      />
    </div>
  );
}
''')

    print("Screens 06-10 created!")

create_screens_part3()
