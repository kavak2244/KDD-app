import React from 'react';
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
