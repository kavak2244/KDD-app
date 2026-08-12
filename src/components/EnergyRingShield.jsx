import React from 'react';

export default function EnergyRingShield({ isArmed, isAlarm = false, size = 120 }) {
  // Theme colors based on state
  const primaryColor = isAlarm ? '#EF4444' : isArmed ? '#22C55E' : '#1F6BFF';
  const secondaryColor = isAlarm ? '#F87171' : isArmed ? '#4ADE80' : '#60A5FA';
  const glowFilter = isAlarm
    ? 'drop-shadow(0 0 18px rgba(239, 68, 68, 0.85))'
    : isArmed
    ? 'drop-shadow(0 0 20px rgba(34, 197, 94, 0.75)) drop-shadow(0 0 35px rgba(31, 107, 255, 0.5))'
    : 'drop-shadow(0 0 18px rgba(31, 107, 255, 0.75))';

  return (
    <div
      className="relative flex items-center justify-center select-none"
      style={{ width: size, height: size }}
    >
      {/* 1. Ambient Background Radial Glow */}
      <div
        className="absolute inset-0 rounded-full blur-xl pointer-events-none transition-all duration-500"
        style={{
          background: isAlarm
            ? 'radial-gradient(circle, rgba(239,68,68,0.35) 0%, transparent 70%)'
            : isArmed
            ? 'radial-gradient(circle, rgba(34,197,94,0.3) 0%, rgba(31,107,255,0.2) 50%, transparent 70%)'
            : 'radial-gradient(circle, rgba(31,107,255,0.3) 0%, transparent 70%)',
        }}
      />

      {/* 2. SVG Vector Energy Rings & Shield */}
      <svg
        viewBox="0 0 200 200"
        className="w-full h-full relative z-10 transition-transform duration-500 hover:scale-105"
        style={{ filter: glowFilter }}
      >
        <defs>
          {/* Gradients */}
          <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#1E293B" stopOpacity="0.9" />
            <stop offset="50%" stopColor="#0F172A" stopOpacity="0.95" />
            <stop offset="100%" stopColor="#020617" stopOpacity="1" />
          </linearGradient>

          <linearGradient id="shieldBorderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor={secondaryColor} />
            <stop offset="50%" stopColor={primaryColor} />
            <stop offset="100%" stopColor="#1E293B" />
          </linearGradient>

          <linearGradient id="ringGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor={primaryColor} />
            <stop offset="50%" stopColor={secondaryColor} />
            <stop offset="100%" stopColor="#1F6BFF" />
          </linearGradient>

          <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feMerge>
              <feMergeNode in="blur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
        </defs>

        {/* Outer Rotating Energy Ring 1 */}
        <circle
          cx="100"
          cy="100"
          r="92"
          fill="none"
          stroke="url(#ringGrad)"
          strokeWidth="2"
          strokeDasharray="14 10 4 10"
          className="origin-center animate-[spin_12s_linear_infinite]"
          opacity="0.85"
        />

        {/* Middle Energy Ring 2 */}
        <circle
          cx="100"
          cy="100"
          r="82"
          fill="none"
          stroke={primaryColor}
          strokeWidth="3"
          strokeDasharray="40 15 20 15"
          className="origin-center animate-[spin_8s_linear_infinite_reverse]"
          opacity="0.95"
        />

        {/* Inner Solid Luminous Ring */}
        <circle
          cx="100"
          cy="100"
          r="72"
          fill="none"
          stroke={secondaryColor}
          strokeWidth="1.5"
          opacity="0.6"
        />

        {/* Subtle decorative orbital ticks */}
        <g stroke={primaryColor} strokeWidth="2" opacity="0.7">
          <line x1="100" y1="5" x2="100" y2="12" />
          <line x1="100" y1="188" x2="100" y2="195" />
          <line x1="5" y1="100" x2="12" y2="100" />
          <line x1="188" y1="100" x2="195" y2="100" />
        </g>

        {/* 3D Shield Background Container */}
        <path
          d="M 100 35 L 148 55 C 148 100 135 138 100 162 C 65 138 52 100 52 55 Z"
          fill="url(#shieldGrad)"
          stroke="url(#shieldBorderGrad)"
          strokeWidth="3.5"
          strokeLinejoin="round"
        />

        {/* Inner Shield Bevel Layer */}
        <path
          d="M 100 45 L 140 62 C 140 98 128 128 100 148 C 72 128 60 98 60 62 Z"
          fill="none"
          stroke={primaryColor}
          strokeWidth="1.5"
          opacity="0.7"
        />

        {/* Central Luminous Checkmark Icon */}
        <path
          d="M 82 100 L 94 114 L 122 84"
          fill="none"
          stroke="#FFFFFF"
          strokeWidth="6.5"
          strokeLinecap="round"
          strokeLinejoin="round"
          style={{
            filter: `drop-shadow(0 0 8px ${secondaryColor}) drop-shadow(0 0 16px ${primaryColor})`,
          }}
        />

        {/* Floating Particle Accents */}
        <circle cx="48" cy="85" r="2" fill={secondaryColor} className="animate-ping" opacity="0.8" />
        <circle cx="152" cy="115" r="2.5" fill={primaryColor} className="animate-pulse" opacity="0.9" />
        <circle cx="70" cy="148" r="1.5" fill="#FFFFFF" opacity="0.7" />
        <circle cx="130" cy="50" r="2" fill={secondaryColor} opacity="0.8" />
      </svg>
    </div>
  );
}
