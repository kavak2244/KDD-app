import React from 'react';
import { Home, Shield, Zap, Settings } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function BottomNavigation({ activeTab, onSelectTab }) {
  const tabs = [
    { id: 'dashboard', label: 'خانه', icon: Home },
    { id: 'status', label: 'وضعیت', icon: Shield },
    { id: 'outputs', label: 'خروجی‌ها', icon: Zap },
    { id: 'settings', label: 'تنظیمات', icon: Settings },
  ];

  return (
    <div className="sticky bottom-0 left-0 right-0 z-30 bg-[#0D1117]/95 backdrop-blur-xl border-t border-[#2D333B] px-3 py-2 flex items-center justify-around">
      {tabs.map((tab) => {
        const Icon = tab.icon;
        const isActive = activeTab === tab.id;
        return (
          <button
            key={tab.id}
            onClick={() => {
              playSound('click');
              onSelectTab(tab.id);
            }}
            className={`flex flex-col items-center justify-center flex-1 py-1 rounded-xl transition-all duration-200 relative ${
              isActive ? 'text-[#1F6BFF]' : 'text-gray-400 hover:text-gray-200'
            }`}
          >
            <div className="relative">
              <Icon className={`w-5 h-5 transition-transform duration-200 ${isActive ? 'scale-110 stroke-[2.4]' : 'stroke-[1.8]'}`} />
              {isActive && (
                <span className="absolute -bottom-1.5 left-1/2 -translate-x-1/2 w-1.5 h-1.5 bg-[#1F6BFF] rounded-full shadow-[0_0_8px_#1F6BFF]" />
              )}
            </div>
            <span className={`text-[11px] mt-1 font-medium ${isActive ? 'text-[#1F6BFF] font-semibold' : 'text-gray-400'}`}>
              {tab.label}
            </span>
          </button>
        );
      })}
    </div>
  );
}
