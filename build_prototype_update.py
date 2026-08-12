import os

def update_all():
    # 1. Screen01_Splash.jsx
    with open('/home/user/kdd-prototype/src/screens/Screen01_Splash.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useEffect } from 'react';
import { playSound } from '../utils/audio';

export default function Screen01_Splash({ onFinish }) {
  // Auto-advance to My Devices after 2.2 seconds
  useEffect(() => {
    const timer = setTimeout(() => {
      playSound('click');
      onFinish();
    }, 2200);
    return () => clearTimeout(timer);
  }, [onFinish]);

  return (
    <div
      onClick={() => {
        playSound('click');
        onFinish();
      }}
      className="min-h-full flex flex-col items-center justify-center p-6 bg-[#090D14] text-center relative overflow-hidden cursor-pointer select-none"
    >
      {/* Radial background glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-[#1F6BFF]/15 rounded-full blur-3xl pointer-events-none" />

      {/* Main Logo Image */}
      <div className="relative z-10 flex flex-col items-center animate-scaleUp">
        <div className="relative w-64 h-64 flex items-center justify-center mb-2">
          <img
            src="/assets/logo_full.png"
            alt="KDD Smart Security Logo"
            className="w-full h-full object-contain drop-shadow-[0_15px_30px_rgba(0,0,0,0.9)] transition-transform duration-700 hover:scale-105"
          />
        </div>

        {/* Loading Spinner & Status */}
        <div className="mt-8 flex flex-col items-center gap-3">
          <div className="w-6 h-6 border-2 border-[#1F6BFF]/30 border-t-[#1F6BFF] rounded-full animate-spin shadow-[0_0_10px_#1F6BFF]" />
          <span className="text-xs text-gray-400 font-medium">در حال بارگذاری سامانه KDD...</span>
        </div>
      </div>
    </div>
  );
}
''')

    # 2. Screen02_MyDevices.jsx (Clean, exact match to 02_دستگاه_های_من.jpg + Password Modal)
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
    // Accept user password or default demo password '1234' or any valid entry
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
    <div className="min-h-full flex flex-col p-5 bg-[#0D1117] text-right relative">
      {/* Top Header matching 02_دستگاه_های_من.jpg */}
      <div className="mb-6 pt-1">
        <div className="text-left mb-2">
          <span className="text-sm font-extrabold text-white tracking-widest">KDD</span>
        </div>
        <h2 className="text-xl font-bold text-white text-center mb-1">دستگاه‌های من</h2>
        <p className="text-xs text-gray-400 text-center">
          برای ورود، یکی از دستگاه‌ها را انتخاب کنید
        </p>
      </div>

      {/* Devices List (Exact styling from Image 02) */}
      <div className="flex-1 space-y-3 overflow-y-auto pb-4">
        {devices.map((dev) => (
          <div
            key={dev.id}
            onClick={() => handleDeviceClick(dev)}
            className="p-4 rounded-2xl bg-[#161B22] border border-[#2D333B] hover:border-[#1F6BFF] hover:shadow-[0_0_20px_rgba(31,107,255,0.2)] transition-all cursor-pointer flex items-center justify-between group"
          >
            {/* Left: Chevron Arrow */}
            <div className="flex items-center">
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
            <div className="w-11 h-11 rounded-xl bg-[#0D1117] border border-[#2D333B] text-[#1F6BFF] flex items-center justify-center group-hover:border-[#1F6BFF]/40 group-hover:shadow-[0_0_10px_rgba(31,107,255,0.3)] transition-all">
              <Shield className="w-5 h-5" />
            </div>
          </div>
        ))}

        {/* Add New Device Button (matching Image 02) */}
        <button
          onClick={() => {
            playSound('click');
            onAddNew();
          }}
          className="w-full p-4 rounded-2xl border border-dashed border-[#2D333B] hover:border-[#1F6BFF] bg-[#161B22]/50 hover:bg-[#161B22] text-[#1F6BFF] transition-all flex items-center justify-center gap-2 group mt-2"
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
            {/* Modal Header */}
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
              رمز عبور دستگاه را وارد کنید یا از حسگر اثر انگشت استفاده نمایید:
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
                  رمز عبور نادرست است (حداقل ۴ رقم)
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

    # 3. Screen05_RegisterStep3.jsx (Step 3 completes and returns to My Devices page!)
    with open('/home/user/kdd-prototype/src/screens/Screen05_RegisterStep3.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState } from 'react';
import { ArrowRight, ChevronLeft, Check, Lock, Eye, EyeOff, Fingerprint, Info, CheckCircle2 } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen05_RegisterStep3({ formData, setFormData, onComplete, onBack }) {
  const [showPass, setShowPass] = useState(false);
  const [showConfirmPass, setShowConfirmPass] = useState(false);

  const getPasswordStrength = (pass) => {
    if (!pass) return { score: 0, text: 'رمز وارد نشده', color: 'bg-gray-600' };
    if (pass.length < 4) return { score: 1, text: 'ضعیف', color: 'bg-red-500' };
    if (pass.length < 7) return { score: 2, text: 'متوسط', color: 'bg-[#1F6BFF]' };
    return { score: 4, text: 'قوی و امن', color: 'bg-emerald-500' };
  };

  const strength = getPasswordStrength(formData.password || '');

  const handleSubmit = () => {
    playSound('arm');
    onComplete();
  };

  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      {/* Top Bar */}
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
        <h2 className="text-base font-bold text-white">تعیین رمز عبور</h2>
        <div className="w-8" />
      </div>

      <p className="text-xs text-gray-400 mb-5 text-center">
        برای افزایش امنیت، یک رمز عبور برای ورود به اپلیکیشن تعیین کنید
      </p>

      {/* Stepper (3 Steps) */}
      <div className="flex items-center justify-between mb-6 px-4">
        {/* Step 3 (Active) */}
        <div className="flex flex-col items-center">
          <div className="w-7 h-7 rounded-full bg-[#1F6BFF] text-white flex items-center justify-center text-xs font-bold shadow-[0_0_12px_#1F6BFF] mb-1">
            ۳
          </div>
          <span className="text-[10px] text-[#1F6BFF] font-bold">تعیین رمز</span>
        </div>
        <div className="flex-1 h-0.5 bg-emerald-500 mx-2" />

        {/* Step 2 (Completed) */}
        <div className="flex flex-col items-center">
          <div className="w-7 h-7 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs font-bold mb-1">
            <Check className="w-4 h-4" />
          </div>
          <span className="text-[10px] text-emerald-400 font-medium">اطلاعات گارانتی</span>
        </div>
        <div className="flex-1 h-0.5 bg-emerald-500 mx-2" />

        {/* Step 1 (Completed) */}
        <div className="flex flex-col items-center">
          <div className="w-7 h-7 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs font-bold mb-1">
            <Check className="w-4 h-4" />
          </div>
          <span className="text-[10px] text-emerald-400 font-medium">ثبت دستگاه</span>
        </div>
      </div>

      {/* Fields */}
      <div className="flex-1 space-y-4 overflow-y-auto pb-4">
        {/* Password */}
        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1.5">
            رمز عبور
          </label>
          <div className="relative">
            <input
              type={showPass ? 'text' : 'password'}
              dir="ltr"
              value={formData.password || ''}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              placeholder="رمز عبور را وارد کنید"
              className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3.5 py-3 text-sm text-white font-mono placeholder:text-gray-600 outline-none transition-colors pr-10"
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

          {/* Password Strength Meter */}
          <div className="mt-2 flex items-center justify-between text-xs">
            <span className={`text-[11px] font-semibold ${
              strength.score === 1 ? 'text-red-400' : strength.score === 2 ? 'text-blue-400' : strength.score >= 3 ? 'text-emerald-400' : 'text-gray-500'
            }`}>
              {strength.text}
            </span>
            <div className="flex gap-1.5">
              {[1, 2, 3, 4].map((step) => (
                <div
                  key={step}
                  className={`w-6 h-1.5 rounded-full transition-all ${
                    strength.score >= step ? strength.color : 'bg-gray-700'
                  }`}
                />
              ))}
            </div>
          </div>
        </div>

        {/* Retype Password */}
        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1.5">
            تکرار رمز عبور
          </label>
          <div className="relative">
            <input
              type={showConfirmPass ? 'text' : 'password'}
              dir="ltr"
              value={formData.confirmPassword || ''}
              onChange={(e) => setFormData({ ...formData, confirmPassword: e.target.value })}
              placeholder="رمز عبور را مجدداً وارد کنید"
              className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3.5 py-3 text-sm text-white font-mono placeholder:text-gray-600 outline-none transition-colors pr-10"
            />
            <button
              type="button"
              onClick={() => setShowConfirmPass(!showConfirmPass)}
              className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white"
            >
              {showConfirmPass ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
            </button>
            <Lock className="w-4 h-4 text-gray-500 absolute right-3 top-1/2 -translate-y-1/2" />
          </div>
        </div>

        {/* Biometric Toggle Card */}
        <div className="p-4 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <div className="flex items-center gap-3">
            <button
              type="button"
              onClick={() => {
                playSound('click');
                setFormData({ ...formData, biometric: !formData.biometric });
              }}
              className={`w-12 h-6 rounded-full transition-colors relative p-0.5 ${
                formData.biometric ? 'bg-[#1F6BFF]' : 'bg-[#2D333B]'
              }`}
            >
              <div className={`w-5 h-5 rounded-full bg-white transition-transform ${
                formData.biometric ? '-translate-x-6' : 'translate-x-0'
              }`} />
            </button>
          </div>

          <div className="text-right">
            <h4 className="text-xs font-bold text-white mb-0.5">فعال‌سازی اثر انگشت</h4>
            <p className="text-[11px] text-gray-400">ورود با اثر انگشت</p>
          </div>

          <div className="w-10 h-10 rounded-xl bg-[#1F6BFF]/10 text-[#1F6BFF] flex items-center justify-center">
            <Fingerprint className="w-5 h-5" />
          </div>
        </div>

        {/* Info Banner */}
        <div className="p-3 rounded-xl bg-[#161B22]/60 border border-[#2D333B] flex items-center gap-2.5 text-gray-400 text-xs">
          <Info className="w-4 h-4 text-[#1F6BFF] shrink-0" />
          <p className="text-[11px] leading-relaxed">
            رمز عبور شما به‌صورت امن روی دستگاه نگهداری می‌شود.
          </p>
        </div>
      </div>

      {/* Complete Button -> Returns to My Devices */}
      <div className="pt-3">
        <button
          onClick={handleSubmit}
          className="w-full py-3.5 px-6 rounded-2xl bg-[#1F6BFF] hover:bg-[#1A5BDB] text-white font-bold text-sm shadow-[0_0_25px_rgba(31,107,255,0.5)] transition-all flex items-center justify-center gap-2"
        >
          <span>ثبت و ادامه</span>
          <ChevronLeft className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
}
''')

    # 4. Screen06_Dashboard.jsx (Exact replica of 06_داشبورد___خانه.jpg, minimal, luxury, un-cluttered!)
    with open('/home/user/kdd-prototype/src/screens/Screen06_Dashboard.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React from 'react';
import { Shield, Bell, CheckCircle2 } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen06_Dashboard({
  device,
  isArmed,
  onToggleArm,
  onOpenNotifications,
  unreadCount = 0,
}) {
  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right select-none">
      {/* Top Bar (matching Image 06: KDD on top-left, Bell on top-right) */}
      <div className="flex items-center justify-between mb-3 pt-1">
        <button
          onClick={() => {
            playSound('click');
            onOpenNotifications();
          }}
          className="relative p-2 text-gray-300 hover:text-white transition-colors"
        >
          <Bell className="w-5 h-5 stroke-[1.8]" />
          {unreadCount > 0 && (
            <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-red-500 rounded-full shadow-[0_0_6px_#EF4444]" />
          )}
        </button>

        <span className="text-base font-extrabold text-white tracking-widest">KDD</span>
      </div>

      {/* Main Content Area */}
      <div className="flex-1 space-y-4 overflow-y-auto pb-2 flex flex-col justify-between">
        {/* Top Hero Container (Truck + Device Name + Status Chip + 2 Metrics) */}
        <div className="rounded-3xl bg-[#161B22] border border-[#2D333B] p-4 relative overflow-hidden shadow-xl">
          {/* Top Half of Card: Truck on Left, Name & Status on Right */}
          <div className="flex items-center justify-between mb-4">
            {/* Right: Device Title & Status */}
            <div className="text-right flex flex-col items-end">
              <h1 className="text-3xl font-black text-white mb-2 tracking-tight">
                {device?.name?.split('—')[0]?.trim() || 'FH500'}
              </h1>
              
              {/* Status Chip: سیستم متصل است */}
              <div className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-emerald-950/40 border border-emerald-600/40 text-emerald-400 text-xs font-semibold shadow-[0_0_15px_rgba(34,197,94,0.15)]">
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                <span>سیستم متصل است</span>
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
              </div>
            </div>

            {/* Left: Truck Visual with glowing Blue Energy Ring under it */}
            <div className="relative w-36 h-36 flex items-center justify-center">
              <img
                src="/assets/truck_fh500.png"
                alt="Truck FH500"
                className="w-full h-full object-contain mix-blend-lighten z-10 drop-shadow-[0_10px_20px_rgba(0,0,0,0.8)]"
              />
            </div>
          </div>

          {/* Bottom Half of Card: 2 Metric Cards side by side */}
          <div className="grid grid-cols-2 gap-3 pt-3 border-t border-[#2D333B]/70">
            {/* Left Metric: باتری دستگاه ۹۸٪ */}
            <div className="p-3 rounded-2xl bg-[#0D1117]/90 border border-[#2D333B] flex items-center justify-between">
              {/* Battery Graphic Icon */}
              <div className="w-6 h-9 rounded-md border-2 border-emerald-400 p-0.5 flex flex-col justify-end relative">
                <div className="absolute -top-1 left-1/2 -translate-x-1/2 w-2.5 h-1 bg-emerald-400 rounded-t-sm" />
                <div className="w-full h-4/5 bg-emerald-400 rounded-sm shadow-[0_0_8px_#22C55E]" />
              </div>

              <div className="text-right">
                <span className="text-[11px] text-gray-400 block mb-0.5">باتری دستگاه</span>
                <span className="text-lg font-black text-white font-mono">{device?.battery || 98}٪</span>
              </div>
            </div>

            {/* Right Metric: سیگنال GSM عالی */}
            <div className="p-3 rounded-2xl bg-[#0D1117]/90 border border-[#2D333B] flex items-center justify-between">
              {/* GSM Signal Bars Graphic */}
              <div className="flex items-end gap-1 h-6">
                <div className="w-1.5 h-2 bg-[#1F6BFF] rounded-sm" />
                <div className="w-1.5 h-3.5 bg-[#1F6BFF] rounded-sm" />
                <div className="w-1.5 h-5 bg-[#1F6BFF] rounded-sm" />
                <div className="w-1.5 h-6 bg-[#1F6BFF] rounded-sm shadow-[0_0_8px_#1F6BFF]" />
              </div>

              <div className="text-right">
                <span className="text-[11px] text-gray-400 block mb-0.5">سیگنال GSM</span>
                <span className="text-base font-black text-white">عالی</span>
              </div>
            </div>
          </div>
        </div>

        {/* Protection Status Card (Bottom Half - Exact match to Image 06) */}
        <div className="rounded-3xl bg-[#161B22] border border-[#2D333B] p-5 relative overflow-hidden shadow-2xl flex items-center justify-between min-h-[220px]">
          {/* Left: Glowing Blue Energy Ring with Shield inside */}
          <div className="relative w-36 h-36 flex items-center justify-center">
            <img
              src="/assets/shield_ring.png"
              alt="Blue Energy Shield"
              className={`w-full h-full object-contain mix-blend-lighten transition-transform duration-500 ${
                isArmed ? 'scale-105 filter drop-shadow-[0_0_20px_#1F6BFF]' : 'opacity-60 scale-95'
              }`}
            />
          </div>

          {/* Right: Security Protection Status & Big Switch */}
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

              <p className="text-xs text-gray-400 mb-6">
                {isArmed ? 'حفاظت خودرو فعال است' : 'حفاظت خودرو غیرفعال است'}
              </p>
            </div>

            {/* Blue Pill Toggle Switch */}
            <button
              type="button"
              onClick={() => {
                onToggleArm();
              }}
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

    print("Updated Screens 01, 02, 05, 06 written successfully!")

update_all()
