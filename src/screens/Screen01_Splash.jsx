import React, { useEffect } from 'react';
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
