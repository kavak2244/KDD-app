import React, { useState } from 'react';
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
