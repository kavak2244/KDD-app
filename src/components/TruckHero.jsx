import React from 'react';
import { ASSET_VOLVO_FINAL_TRANSPARENT } from '../assetsBase64';

export default function TruckHero({ className = '' }) {
  return (
    <div className={`relative w-44 h-36 sm:w-48 sm:h-40 flex items-center justify-center select-none ${className}`}>
      {/* 1. Luminous Circular Energy Ring on Floor (Centered directly under the truck wheels) */}
      <svg
        viewBox="0 0 200 90"
        className="absolute -bottom-1 w-44 h-16 pointer-events-none z-0"
        style={{
          filter: 'drop-shadow(0 0 8px #00e5ff) drop-shadow(0 0 18px rgba(0, 229, 255, 0.6))',
        }}
      >
        {/* Outer Orbiting Energy Ring */}
        <ellipse
          cx="100"
          cy="48"
          rx="86"
          ry="28"
          fill="none"
          stroke="#00e5ff"
          strokeWidth="3.5"
          strokeDasharray="20 10 6 10"
          className="animate-[spin_14s_linear_infinite] origin-[100px_48px]"
        />
        {/* Inner Solid Luminous Ring */}
        <ellipse
          cx="100"
          cy="48"
          rx="76"
          ry="23"
          fill="none"
          stroke="#00b4d8"
          strokeWidth="2"
          opacity="0.8"
        />
        {/* Floor Radial Glow */}
        <ellipse
          cx="100"
          cy="48"
          rx="66"
          ry="18"
          fill="rgba(0, 229, 255, 0.2)"
        />
      </svg>

      {/* 2. Headlight Light Reflections on Card Floor */}
      <div className="absolute bottom-3 left-6 w-12 h-6 bg-cyan-400/25 rounded-full blur-md transform -rotate-12 pointer-events-none" />
      <div className="absolute bottom-3 right-6 w-12 h-6 bg-cyan-400/25 rounded-full blur-md transform rotate-12 pointer-events-none" />

      {/* 3. Pure Cutout Volvo Truck (Centered on the ring) */}
      <img
        src={ASSET_VOLVO_FINAL_TRANSPARENT}
        alt="Volvo FH500 KDD Truck"
        className="w-full h-full object-contain relative z-10 filter drop-shadow-[0_15px_30px_rgba(0,0,0,0.95)] transition-transform duration-500 hover:scale-105"
      />
    </div>
  );
}
