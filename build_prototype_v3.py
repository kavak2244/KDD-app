import os

def build_refined_prototype():
    # 1. Screen01_Splash.jsx
    with open('/home/user/kdd-prototype/src/screens/Screen01_Splash.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useEffect } from 'react';
import { ASSET_LOGO_FULL } from '../assetsBase64';
import { playSound } from '../utils/audio';

export default function Screen01_Splash({ onFinish }) {
  useEffect(() => {
    const timer = setTimeout(() => {
      playSound('click');
      onFinish();
    }, 2400);
    return () => clearTimeout(timer);
  }, [onFinish]);

  return (
    <div
      onClick={() => {
        playSound('click');
        onFinish();
      }}
      className="min-h-full flex flex-col items-center justify-between p-6 bg-[#080B10] text-center relative overflow-hidden cursor-pointer select-none"
    >
      {/* Ambient Blue Backlight */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[340px] h-[340px] bg-[#1F6BFF]/20 rounded-full blur-[90px] pointer-events-none" />

      {/* Top spacer */}
      <div className="w-full pt-2 flex justify-end">
        <span className="text-[10px] text-gray-500 font-mono tracking-wider">KDD SECURE SYSTEM</span>
      </div>

      {/* Center: Full Official Logo with Truck & Shield */}
      <div className="relative z-10 flex flex-col items-center my-auto">
        <div className="relative w-64 max-w-[270px] aspect-square flex items-center justify-center mb-4 transition-transform duration-700 hover:scale-105">
          <img
            src={ASSET_LOGO_FULL}
            alt="KDD Smart Security Logo"
            className="w-full h-full object-contain filter drop-shadow-[0_20px_40px_rgba(0,0,0,0.9)]"
          />
        </div>

        {/* Loading Spinner */}
        <div className="mt-6 flex flex-col items-center gap-2.5">
          <div className="w-6 h-6 border-2 border-[#1F6BFF]/20 border-t-[#1F6BFF] rounded-full animate-spin shadow-[0_0_12px_#1F6BFF]" />
          <span className="text-xs text-gray-400 font-medium">در حال اتصال به سامانه...</span>
        </div>
      </div>

      {/* Bottom Hint */}
      <div className="w-full pb-3 text-center">
        <span className="text-[11px] text-gray-500 hover:text-gray-400 transition-colors">
          برای ورود سریع، روی صفحه ضربه بزنید
        </span>
      </div>
    </div>
  );
}
''')

    # 2. Screen02_MyDevices.jsx
    with open('/home/user/kdd-prototype/src/screens/Screen02_MyDevices.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState } from 'react';
import { Shield, ChevronLeft, Plus, Lock, Fingerprint, Eye, EyeOff, X, ArrowRight } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen02_MyDevices({ devices, activeDeviceId, onSelectDevice, onAddNew }) {
  const [selectedForLogin, setSelectedForLogin] = useState(null);
  const [enteredPass, setEnteredPass] = useState('');
  const [showPass, setShowPass] = useState(false);
  const [passError, setPassError] = useState(false);

  const handleDeviceClick = (dev) => {
    playSound('click');
    setSelectedForLogin(dev);
    setEnteredPass('');
    setPassError(false);
  };

  const handleUnlockSubmit = (e) => {
    e?.preventDefault();
    if (enteredPass.trim().length >= 4 || enteredPass === '1234' || enteredPass === selectedForLogin.password) {
      playSound('arm');
      onSelectDevice(selectedForLogin.id);
      setSelectedForLogin(null);
    } else {
      playSound('alarm');
      setPassError(true);
    }
  };

  const handleBiometricUnlock = () => {
    playSound('arm');
    onSelectDevice(selectedForLogin.id);
    setSelectedForLogin(null);
  };

  return (
    <div className="min-h-full flex flex-col p-5 bg-[#0D1117] text-right relative select-none">
      {/* Top Header matching Image 02 */}
      <div className="mb-5 pt-1">
        <div className="text-left mb-3">
          <span className="text-sm font-extrabold text-white tracking-widest font-sans">KDD</span>
        </div>
        <h2 className="text-xl font-bold text-white text-center mb-1">دستگاه‌های من</h2>
        <p className="text-xs text-gray-400 text-center">
          برای ورود، یکی از دستگاه‌ها را انتخاب کنید
        </p>
      </div>

      {/* Devices List (clean, standard industrial cards) */}
      <div className="flex-1 space-y-3 overflow-y-auto pb-4">
        {devices.map((dev) => (
          <div
            key={dev.id}
            onClick={() => handleDeviceClick(dev)}
            className="p-4 rounded-2xl bg-[#161B22] border border-[#242C37] hover:border-[#1F6BFF] hover:shadow-[0_0_20px_rgba(31,107,255,0.2)] transition-all duration-200 cursor-pointer flex items-center justify-between group"
          >
            {/* Left: Chevron Arrow */}
            <div className="flex items-center pl-1">
              <ChevronLeft className="w-5 h-5 text-gray-500 group-hover:text-[#1F6BFF] group-hover:-translate-x-1 transition-all" />
            </div>

            {/* Center: Device Name & Serial */}
            <div className="flex-1 pr-3 text-right">
              <h3 className="text-base font-bold text-white mb-0.5">{dev.name.split('—')[0].trim()}</h3>
              <p className="text-xs text-gray-400 font-mono" dir="rtl">
                سریال: {dev.serial}
              </p>
            </div>

            {/* Right: Shield Outline Icon */}
            <div className="w-11 h-11 rounded-xl bg-[#0E131A] border border-[#2D333B] text-[#1F6BFF] flex items-center justify-center group-hover:border-[#1F6BFF]/50 group-hover:shadow-[0_0_12px_rgba(31,107,255,0.3)] transition-all">
              <Shield className="w-5 h-5 stroke-[1.8]" />
            </div>
          </div>
        ))}

        {/* Add New Device Button (matching Image 02) */}
        <button
          onClick={() => {
            playSound('click');
            onAddNew();
          }}
          className="w-full p-4 rounded-2xl border border-dashed border-[#2D333B] hover:border-[#1F6BFF] bg-[#161B22]/40 hover:bg-[#161B22] text-[#1F6BFF] transition-all flex items-center justify-center gap-2 group mt-2"
        >
          <span className="text-sm font-bold">افزودن دستگاه جدید</span>
          <div className="w-7 h-7 rounded-full border border-dashed border-[#1F6BFF] flex items-center justify-center group-hover:scale-110 transition-transform">
            <Plus className="w-4 h-4 text-[#1F6BFF]" />
          </div>
        </button>
      </div>

      {/* Password Prompt Modal */}
      {selectedForLogin && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md animate-fadeIn">
          <div className="w-full max-w-xs bg-[#161B22] border border-[#2D333B] rounded-3xl p-5 text-right shadow-2xl animate-scaleUp">
            {/* Header */}
            <div className="flex items-center justify-between mb-4 pb-2 border-b border-[#2D333B]">
              <button
                onClick={() => setSelectedForLogin(null)}
                className="p-1 rounded-lg text-gray-400 hover:text-white"
              >
                <X className="w-4 h-4" />
              </button>
              <div className="flex items-center gap-2">
                <span className="text-xs font-bold text-white">ورود امن به {selectedForLogin.name.split('—')[0]}</span>
                <Lock className="w-4 h-4 text-[#1F6BFF]" />
              </div>
            </div>

            <p className="text-xs text-gray-400 mb-4 leading-relaxed">
              رمز عبور دستگاه را وارد کنید:
            </p>

            <form onSubmit={handleUnlockSubmit} className="space-y-4">
              <div className="relative">
                <input
                  type={showPass ? 'text' : 'password'}
                  dir="ltr"
                  autoFocus
                  value={enteredPass}
                  onChange={(e) => {
                    setEnteredPass(e.target.value);
                    setPassError(false);
                  }}
                  placeholder="••••••"
                  className={`w-full bg-[#0D1117] border rounded-xl px-3.5 py-3 text-sm text-white font-mono placeholder:text-gray-600 outline-none pr-10 text-center tracking-widest ${
                    passError ? 'border-red-500 focus:border-red-500' : 'border-[#2D333B] focus:border-[#1F6BFF]'
                  }`}
                />
                <button
                  type="button"
                  onClick={() => setShowPass(!showPass)}
                  className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white"
                >
                  {showPass ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                </button>
                <Lock className="w-4 h-4 text-gray-500 absolute right-3 top-1/2 -translate-y-1/2" />
              </div>

              {passError && (
                <p className="text-[11px] text-red-400 text-center">
                  رمز عبور وارد شده نادرست است
                </p>
              )}

              {/* Biometric Quick Button */}
              <button
                type="button"
                onClick={handleBiometricUnlock}
                className="w-full py-2.5 rounded-xl bg-[#0D1117] border border-[#2D333B] hover:border-[#1F6BFF] text-gray-300 hover:text-white text-xs font-semibold flex items-center justify-center gap-2 transition-colors"
              >
                <Fingerprint className="w-4 h-4 text-[#1F6BFF]" />
                <span>ورود سریع با اثر انگشت</span>
              </button>

              {/* Submit Button */}
              <button
                type="submit"
                className="w-full py-3 rounded-xl bg-[#1F6BFF] hover:bg-[#1A5BDB] text-white text-xs font-bold shadow-[0_0_15px_#1F6BFF] transition-all flex items-center justify-center gap-2"
              >
                <span>تأیید و ورود به داشبورد</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
''')

    # 3. Screen06_Dashboard.jsx (Pixel perfect replica of 06_داشبورد___خانه.jpg)
    with open('/home/user/kdd-prototype/src/screens/Screen06_Dashboard.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React from 'react';
import { Shield, Bell, CheckCircle2 } from 'lucide-react';
import { ASSET_TRUCK_FH500, ASSET_SHIELD_RING } from '../assetsBase64';
import { playSound } from '../utils/audio';

export default function Screen06_Dashboard({
  device,
  isArmed,
  onToggleArm,
  onOpenNotifications,
  unreadCount = 0,
}) {
  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right select-none justify-between">
      {/* Top Bar matching Image 06: KDD on top-left, Bell on top-right */}
      <div className="flex items-center justify-between mb-2 pt-1 px-1">
        <button
          onClick={() => {
            playSound('click');
            onOpenNotifications();
          }}
          className="relative p-1.5 text-gray-300 hover:text-white transition-colors"
        >
          <Bell className="w-5 h-5 stroke-[1.8]" />
          {unreadCount > 0 && (
            <span className="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full shadow-[0_0_6px_#EF4444]" />
          )}
        </button>

        <span className="text-base font-extrabold text-white tracking-widest font-sans">KDD</span>
      </div>

      {/* Main 2-Card Content (Exact structure of Image 06) */}
      <div className="flex-1 space-y-4 flex flex-col justify-between py-1">
        {/* Card 1: Top Hero Container (Truck + Device Title + Status Chip + 2 Metrics) */}
        <div className="rounded-3xl bg-[#161B22] border border-[#242C37] p-4 relative overflow-hidden shadow-xl">
          {/* Top Row: Truck on Left, Device Name & Status on Right */}
          <div className="flex items-center justify-between mb-4">
            {/* Left: Heavy Truck with glowing Blue Energy Ring under it */}
            <div className="relative w-36 h-36 flex items-center justify-center">
              <img
                src={ASSET_TRUCK_FH500}
                alt="Volvo FH500"
                className="w-full h-full object-contain mix-blend-lighten z-10 drop-shadow-[0_10px_20px_rgba(0,0,0,0.8)]"
              />
            </div>

            {/* Right: Device Title & Status Chip */}
            <div className="text-right flex flex-col items-end pl-2">
              <h1 className="text-3xl font-black text-white mb-2 tracking-tight font-sans">
                {device?.name?.split('—')[0]?.trim() || 'FH500'}
              </h1>
              
              {/* Status Chip: سیستم متصل است */}
              <div className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-emerald-950/40 border border-emerald-600/40 text-emerald-400 text-xs font-semibold shadow-[0_0_15px_rgba(34,197,94,0.15)]">
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                <span>سیستم متصل است</span>
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 stroke-[2.2]" />
              </div>
            </div>
          </div>

          {/* Bottom Row: 2 Clean Metric Cards side by side */}
          <div className="grid grid-cols-2 gap-3 pt-3 border-t border-[#2D333B]/70">
            {/* Metric 1: باتری دستگاه ۹۸٪ */}
            <div className="p-3 rounded-2xl bg-[#0D1117] border border-[#2D333B] flex items-center justify-between">
              {/* Battery Graphic */}
              <div className="w-6 h-9 rounded-md border-2 border-emerald-400 p-0.5 flex flex-col justify-end relative shadow-[0_0_8px_rgba(34,197,94,0.25)]">
                <div className="absolute -top-1 left-1/2 -translate-x-1/2 w-2.5 h-1 bg-emerald-400 rounded-t-sm" />
                <div className="w-full h-4/5 bg-emerald-400 rounded-sm shadow-[0_0_8px_#22C55E]" />
              </div>

              <div className="text-right">
                <span className="text-[11px] text-gray-400 block mb-0.5 font-medium">باتری دستگاه</span>
                <span className="text-lg font-black text-white font-mono">{device?.battery || 98}٪</span>
              </div>
            </div>

            {/* Metric 2: سیگنال GSM عالی */}
            <div className="p-3 rounded-2xl bg-[#0D1117] border border-[#2D333B] flex items-center justify-between">
              {/* GSM Signal Bars Graphic */}
              <div className="flex items-end gap-1 h-6">
                <div className="w-1.5 h-2 bg-[#1F6BFF] rounded-sm" />
                <div className="w-1.5 h-3.5 bg-[#1F6BFF] rounded-sm" />
                <div className="w-1.5 h-5 bg-[#1F6BFF] rounded-sm" />
                <div className="w-1.5 h-6 bg-[#1F6BFF] rounded-sm shadow-[0_0_8px_#1F6BFF]" />
              </div>

              <div className="text-right">
                <span className="text-[11px] text-gray-400 block mb-0.5 font-medium">سیگنال GSM</span>
                <span className="text-base font-black text-white">عالی</span>
              </div>
            </div>
          </div>
        </div>

        {/* Card 2: Protection Status Card (Exact replica of Image 06) */}
        <div className="rounded-3xl bg-[#161B22] border border-[#242C37] p-5 relative overflow-hidden shadow-2xl flex items-center justify-between min-h-[220px]">
          {/* Left: Glowing Blue Energy Ring Shield */}
          <div className="relative w-36 h-36 flex items-center justify-center">
            <img
              src={ASSET_SHIELD_RING}
              alt="Blue Energy Shield"
              className={`w-full h-full object-contain mix-blend-lighten transition-all duration-500 ${
                isArmed
                  ? 'scale-105 filter drop-shadow-[0_0_25px_#1F6BFF]'
                  : 'opacity-50 scale-95 grayscale-[50%]'
              }`}
            />
          </div>

          {/* Right: Title, Status and Blue Pill Toggle */}
          <div className="text-right flex flex-col items-end justify-between h-full py-1">
            <div>
              {/* Title with Shield Icon */}
              <div className="flex items-center justify-end gap-2 text-gray-200 mb-2">
                <span className="text-sm font-bold">سیستم حفاظتی</span>
                <Shield className="w-4 h-4 text-gray-400 stroke-[2]" />
              </div>

              {/* Status Label (فعال / غیرفعال) */}
              <h2 className={`text-4xl font-black mb-1 transition-colors ${
                isArmed ? 'text-emerald-400 drop-shadow-[0_0_15px_rgba(34,197,94,0.4)]' : 'text-blue-400'
              }`}>
                {isArmed ? 'فعال' : 'غیرفعال'}
              </h2>

              <p className="text-xs text-gray-400 mb-5">
                {isArmed ? 'حفاظت خودرو فعال است' : 'حفاظت خودرو غیرفعال است'}
              </p>
            </div>

            {/* Blue Pill Toggle Switch */}
            <button
              type="button"
              onClick={onToggleArm}
              className={`w-20 h-10 rounded-full p-1 transition-colors duration-300 relative shadow-inner cursor-pointer ${
                isArmed ? 'bg-[#1F6BFF] shadow-[0_0_20px_rgba(31,107,255,0.7)]' : 'bg-[#2D333B]'
              }`}
            >
              <div
                className={`w-8 h-8 rounded-full bg-white transition-transform duration-300 shadow-md ${
                  isArmed ? '-translate-x-10' : 'translate-x-0'
                }`}
              />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
''')

    # 4. DesignSpecView.jsx (Using embedded base64 screen images)
    with open('/home/user/kdd-prototype/src/screens/DesignSpecView.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React from 'react';
import {
  ASSET_SCREEN_01,
  ASSET_SCREEN_02,
  ASSET_SCREEN_03,
  ASSET_SCREEN_04,
  ASSET_SCREEN_05,
  ASSET_SCREEN_06,
  ASSET_SCREEN_07,
  ASSET_SCREEN_08,
  ASSET_SCREEN_09,
  ASSET_SCREEN_10,
  ASSET_SCREEN_11,
  ASSET_SCREEN_12,
  ASSET_SCREEN_13,
  ASSET_SCREEN_14,
} from '../assetsBase64';
import { Palette, Type, Terminal } from 'lucide-react';

export default function DesignSpecView({ onSelectScreen }) {
  const screensList = [
    { num: '01', title: 'Splash / شروع اپ', desc: 'نمایش هویت KDD و حلقه نوری Blue Energy Ring', img: ASSET_SCREEN_01, key: 'splash' },
    { num: '02', title: 'دستگاه‌های من', desc: 'انتخاب دستگاه یا افزودن خودرو جدید', img: ASSET_SCREEN_02, key: 'my-devices' },
    { num: '03', title: 'ثبت دستگاه — مرحله ۱', desc: 'شناسه، نام دستگاه و سیم‌کارت فعال', img: ASSET_SCREEN_03, key: 'register-1' },
    { num: '04', title: 'ثبت گارانتی — مرحله ۲', desc: 'اطلاعات مالک، موقعیت و تکنسین', img: ASSET_SCREEN_04, key: 'register-2' },
    { num: '05', title: 'تعیین رمز عبور — مرحله ۳', desc: 'رمز عبور و فعال‌سازی اثر انگشت', img: ASSET_SCREEN_05, key: 'register-3' },
    { num: '06', title: 'داشبورد / خانه', desc: 'مرکز فرمان اصلی، آلارم، باتری و آنتن', img: ASSET_SCREEN_06, key: 'dashboard' },
    { num: '07', title: 'تنظیمات', desc: 'دسترسی دسته‌بندی‌شده به کلیه زیرسیستم‌ها', img: ASSET_SCREEN_07, key: 'settings' },
    { num: '08', title: 'وضعیت دستگاه', desc: 'تله‌متری زنده ولتاژها، سنسورها و رله‌ها', img: ASSET_SCREEN_08, key: 'status' },
    { num: '09', title: 'خروجی‌ها', desc: 'کنترل و تغییر نام ۸ رله سخت‌افزاری', img: ASSET_SCREEN_09, key: 'outputs' },
    { num: '10', title: 'تنظیمات دستگاه', desc: 'سخت‌افزار، پیامک‌ها، زبان و آژیر', img: ASSET_SCREEN_10, key: 'device-settings' },
    { num: '11', title: 'کدگذاری ریموت', desc: 'شبیه‌ساز فیزیکی توالی کلیدهای ریموت', img: ASSET_SCREEN_11, key: 'remote-coding' },
    { num: '12', title: 'ریموت‌ها', desc: 'مدیریت ۱۰ ریموت، پارتیشن و قفل امنیتی', img: ASSET_SCREEN_12, key: 'remotes' },
    { num: '13', title: 'مخاطبین', desc: 'ماتریس دسترسی مخاطبین (تماس، SMS، ادمین)', img: ASSET_SCREEN_13, key: 'contacts' },
    { num: '14', title: 'سنسورها', desc: 'تنظیم ۸ سنسور (پارتیشن، NO/NC، ۲۴ ساعته)', img: ASSET_SCREEN_14, key: 'sensors' },
  ];

  return (
    <div className="w-full min-h-screen bg-[#080C12] text-gray-200 p-6">
      {/* Header */}
      <div className="max-w-6xl mx-auto mb-8 text-right">
        <div className="flex items-center justify-between mb-3 border-b border-[#2D333B] pb-4">
          <span className="text-xs px-3 py-1 rounded-full bg-[#1F6BFF]/20 text-[#1F6BFF] border border-[#1F6BFF]/40 font-mono">
            KDD Design System v1.1 — Reference Specs
          </span>
          <h1 className="text-2xl font-black text-white">سند طراحی و مشخصات فنی اپلیکیشن KDD</h1>
        </div>
        <p className="text-sm text-gray-400">
          برای تست و اجرای زنده هر صفحه، روی کارت آن کلیک کنید.
        </p>
      </div>

      {/* Design System Tokens Summary */}
      <div className="max-w-6xl mx-auto mb-10 grid grid-cols-1 md:grid-cols-3 gap-4 text-right">
        <div className="p-4 rounded-2xl bg-[#161B22] border border-[#2D333B]">
          <div className="flex items-center gap-2 mb-3 text-[#1F6BFF]">
            <Palette className="w-5 h-5" />
            <h3 className="text-sm font-bold text-white">پالت رنگی برند</h3>
          </div>
          <div className="grid grid-cols-2 gap-2 text-xs font-mono">
            <div className="flex items-center gap-2">
              <span className="w-4 h-4 rounded bg-[#1F6BFF] shadow-[0_0_8px_#1F6BFF]" />
              <span>Primary #1F6BFF</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-4 h-4 rounded bg-[#0D1117] border border-gray-700" />
              <span>Bg #0D1117</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-4 h-4 rounded bg-[#161B22] border border-gray-700" />
              <span>Card #161B22</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-4 h-4 rounded bg-[#22C55E]" />
              <span>Success #22C55E</span>
            </div>
          </div>
        </div>

        <div className="p-4 rounded-2xl bg-[#161B22] border border-[#2D333B]">
          <div className="flex items-center gap-2 mb-3 text-[#1F6BFF]">
            <Type className="w-5 h-5" />
            <h3 className="text-sm font-bold text-white">تایپوگرافی و ساختار RTL</h3>
          </div>
          <ul className="text-xs space-y-1.5 text-gray-300">
            <li>• فونت فارسی: <strong className="text-white">Vazirmatn / IRANYekanX</strong></li>
            <li>• عناوین صفحات: Bold ۲۴px</li>
            <li>• دکمه‌های اصلی: Medium ۱۶px</li>
          </ul>
        </div>

        <div className="p-4 rounded-2xl bg-[#161B22] border border-[#2D333B]">
          <div className="flex items-center gap-2 mb-3 text-[#1F6BFF]">
            <Terminal className="w-5 h-5" />
            <h3 className="text-sm font-bold text-white">لایه ارتباطی ماژول SIM800</h3>
          </div>
          <ul className="text-xs space-y-1.5 text-gray-300">
            <li>• روش ۱: اینترنت ابری (MQTT / TCP Socket)</li>
            <li>• روش ۲: پیامک اضطراری (GSM SMS Fallback)</li>
          </ul>
        </div>
      </div>

      {/* 14 Screens Grid */}
      <div className="max-w-6xl mx-auto">
        <h2 className="text-lg font-bold text-white mb-4 text-right">طرح تمام ۱۴ صفحه اصلی (روی هر صفحه برای تست زنده کلیک کنید):</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-5">
          {screensList.map((sc) => (
            <div
              key={sc.num}
              onClick={() => onSelectScreen(sc.key)}
              className="bg-[#161B22] border border-[#2D333B] hover:border-[#1F6BFF] hover:shadow-[0_0_25px_rgba(31,107,255,0.3)] rounded-2xl overflow-hidden cursor-pointer transition-all flex flex-col group"
            >
              {/* Screen Preview Image */}
              <div className="relative aspect-[9/16] bg-black/60 overflow-hidden">
                <img
                  src={sc.img}
                  alt={sc.title}
                  className="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300"
                />
                <div className="absolute top-3 right-3 px-2 py-0.5 rounded-md bg-black/70 backdrop-blur-md text-[11px] font-mono text-[#1F6BFF] font-bold border border-[#1F6BFF]/40">
                  #{sc.num}
                </div>
                <div className="absolute inset-0 bg-gradient-to-t from-[#161B22] via-transparent to-transparent opacity-80" />
                
                <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between">
                  <span className="text-xs font-bold text-white group-hover:text-[#1F6BFF] transition-colors">
                    تست و تعامل زنده ➔
                  </span>
                </div>
              </div>

              {/* Title and Desc */}
              <div className="p-3 text-right flex-1 flex flex-col justify-between">
                <div>
                  <h3 className="text-sm font-bold text-white mb-1 group-hover:text-[#1F6BFF] transition-colors">{sc.title}</h3>
                  <p className="text-[11px] text-gray-400 leading-relaxed">{sc.desc}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
''')

    print("Refined prototype components created successfully!")

build_refined_prototype()
