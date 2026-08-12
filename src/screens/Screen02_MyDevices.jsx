import React, { useState } from 'react';
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
