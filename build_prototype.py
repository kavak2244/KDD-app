import os

def create_components():
    # 1. BottomNavigation.jsx
    with open('/home/user/kdd-prototype/src/components/BottomNavigation.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React from 'react';
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
''')

    # 2. HardwareTerminal.jsx (Real-time SIM800 / Cloud communication logger)
    with open('/home/user/kdd-prototype/src/components/HardwareTerminal.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState, useEffect, useRef } from 'react';
import { Terminal, Send, Trash2, ChevronUp, ChevronDown, CheckCircle2, MessageSquare, Radio, ShieldAlert } from 'lucide-react';

export default function HardwareTerminal({ logs, onClear, connectionMode, setConnectionMode }) {
  const [isOpen, setIsOpen] = useState(false);
  const [activeTab, setActiveTab] = useState('all'); // all, sms, mqtt, at
  const logEndRef = useRef(null);

  useEffect(() => {
    if (isOpen && logEndRef.current) {
      logEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [logs, isOpen]);

  const filteredLogs = logs.filter(log => {
    if (activeTab === 'all') return true;
    return log.type === activeTab;
  });

  return (
    <div className="w-full bg-[#0D1117] border-t border-[#2D333B] shadow-2xl transition-all duration-300">
      {/* Bar Header */}
      <div className="px-4 py-2.5 bg-[#161B22] border-b border-[#2D333B] flex items-center justify-between">
        <div className="flex items-center gap-3">
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="flex items-center gap-2 text-sm font-semibold text-gray-200 hover:text-[#1F6BFF] transition-colors"
          >
            <Terminal className="w-4 h-4 text-[#1F6BFF]" />
            <span>کنسول ارتباطی SIM800 / سرور ابری KDD</span>
            {isOpen ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
          </button>
          
          <span className="text-xs px-2 py-0.5 rounded-full bg-[#1F6BFF]/20 text-[#1F6BFF] font-mono">
            {logs.length} رویداد
          </span>
        </div>

        <div className="flex items-center gap-2">
          {/* Connection Mode Toggle */}
          <div className="flex items-center bg-[#0D1117] rounded-lg p-0.5 border border-[#2D333B] text-xs">
            <button
              onClick={() => setConnectionMode('internet')}
              className={`flex items-center gap-1.5 px-2.5 py-1 rounded-md transition-all ${
                connectionMode === 'internet'
                  ? 'bg-[#1F6BFF] text-white font-medium shadow-[0_0_10px_rgba(31,107,255,0.5)]'
                  : 'text-gray-400 hover:text-gray-200'
              }`}
            >
              <Radio className="w-3.5 h-3.5" />
              <span>اینترنت (MQTT / Socket)</span>
            </button>
            <button
              onClick={() => setConnectionMode('sms')}
              className={`flex items-center gap-1.5 px-2.5 py-1 rounded-md transition-all ${
                connectionMode === 'sms'
                  ? 'bg-amber-600 text-white font-medium shadow-[0_0_10px_rgba(217,119,6,0.5)]'
                  : 'text-gray-400 hover:text-gray-200'
              }`}
            >
              <MessageSquare className="w-3.5 h-3.5" />
              <span>پیامک (GSM SMS Fallback)</span>
            </button>
          </div>

          <button
            onClick={onClear}
            title="پاک‌کردن لاگ‌ها"
            className="p-1.5 text-gray-400 hover:text-red-400 hover:bg-[#2D333B] rounded-lg transition-colors"
          >
            <Trash2 className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Expanded Console Body */}
      {isOpen && (
        <div className="p-3 bg-[#080C12] max-h-64 overflow-y-auto font-mono text-xs text-left" dir="ltr">
          {/* Filter Chips */}
          <div className="flex gap-2 mb-2 pb-2 border-b border-[#2D333B] text-[11px]" dir="rtl">
            <button
              onClick={() => setActiveTab('all')}
              className={`px-2 py-0.5 rounded ${activeTab === 'all' ? 'bg-[#1F6BFF] text-white' : 'bg-[#161B22] text-gray-400'}`}
            >
              همه ({logs.length})
            </button>
            <button
              onClick={() => setActiveTab('sms')}
              className={`px-2 py-0.5 rounded ${activeTab === 'sms' ? 'bg-amber-600 text-white' : 'bg-[#161B22] text-gray-400'}`}
            >
              دستورات پیامکی SMS
            </button>
            <button
              onClick={() => setActiveTab('mqtt')}
              className={`px-2 py-0.5 rounded ${activeTab === 'mqtt' ? 'bg-emerald-600 text-white' : 'bg-[#161B22] text-gray-400'}`}
            >
              پکت‌های MQTT / JSON
            </button>
            <button
              onClick={() => setActiveTab('at')}
              className={`px-2 py-0.5 rounded ${activeTab === 'at' ? 'bg-purple-600 text-white' : 'bg-[#161B22] text-gray-400'}`}
            >
              فرمان‌های AT Command ماژول
            </button>
          </div>

          {filteredLogs.length === 0 ? (
            <div className="text-gray-500 py-6 text-center italic" dir="rtl">
              هنوز فرمانی ارسال نشده است. دکمه‌ای در اپلیکیشن را لمس کنید تا پکت ارسالی را اینجا مشاهده نمایید.
            </div>
          ) : (
            <div className="space-y-1.5">
              {filteredLogs.map((log, index) => (
                <div
                  key={index}
                  className={`p-2 rounded border flex flex-col gap-1 ${
                    log.type === 'sms'
                      ? 'bg-amber-950/20 border-amber-800/40 text-amber-300'
                      : log.type === 'mqtt'
                      ? 'bg-emerald-950/20 border-emerald-800/40 text-emerald-300'
                      : log.type === 'at'
                      ? 'bg-purple-950/20 border-purple-800/40 text-purple-300'
                      : 'bg-[#161B22] border-[#2D333B] text-gray-300'
                  }`}
                >
                  <div className="flex items-center justify-between text-[10px] text-gray-400">
                    <span className="font-semibold px-1.5 py-0.2 rounded bg-black/40">
                      [{log.type.toUpperCase()}] {log.direction === 'tx' ? 'TX ➔ SENT' : 'RX ➔ RECEIVED'}
                    </span>
                    <span>{log.time}</span>
                  </div>
                  <div className="font-mono break-all select-all font-semibold">
                    {log.payload}
                  </div>
                  {log.description && (
                    <div className="text-[10px] text-gray-400 italic" dir="rtl">
                      💡 {log.description}
                    </div>
                  )}
                </div>
              ))}
              <div ref={logEndRef} />
            </div>
          )}
        </div>
      )}
    </div>
  );
}
''')

    # 3. NotificationDrawer.jsx
    with open('/home/user/kdd-prototype/src/components/NotificationDrawer.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React from 'react';
import { Bell, X, ShieldAlert, Zap, AlertTriangle, CheckCircle, Clock } from 'lucide-react';

export default function NotificationDrawer({ isOpen, onClose, events }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex justify-end bg-black/60 backdrop-blur-sm animate-fadeIn">
      <div className="w-full max-w-sm h-full bg-[#0D1117] border-r border-[#2D333B] flex flex-col shadow-2xl animate-slideLeft">
        {/* Header */}
        <div className="p-4 bg-[#161B22] border-b border-[#2D333B] flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Bell className="w-5 h-5 text-[#1F6BFF]" />
            <h3 className="font-bold text-gray-100">تاریخچه هشدارها و وقایع</h3>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-lg text-gray-400 hover:text-white hover:bg-[#2D333B]"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* List of events */}
        <div className="flex-1 overflow-y-auto p-4 space-y-3">
          {events.length === 0 ? (
            <div className="text-center text-gray-500 py-12">
              هیچ رویدادی ثبت نشده است.
            </div>
          ) : (
            events.map((evt, idx) => (
              <div
                key={idx}
                className="p-3 bg-[#161B22] border border-[#2D333B] rounded-xl flex items-start gap-3 hover:border-gray-600 transition-colors"
              >
                <div className={`p-2 rounded-lg ${
                  evt.level === 'alarm' ? 'bg-red-500/20 text-red-400' :
                  evt.level === 'warning' ? 'bg-amber-500/20 text-amber-400' :
                  'bg-emerald-500/20 text-emerald-400'
                }`}>
                  {evt.level === 'alarm' ? <ShieldAlert className="w-5 h-5" /> :
                   evt.level === 'warning' ? <AlertTriangle className="w-5 h-5" /> :
                   <CheckCircle className="w-5 h-5" />}
                </div>

                <div className="flex-1 min-w-0">
                  <div className="flex items-center justify-between mb-1">
                    <span className="text-xs font-semibold text-gray-200">{evt.title}</span>
                    <span className="text-[10px] text-gray-500 flex items-center gap-1 font-mono">
                      <Clock className="w-3 h-3" />
                      {evt.time}
                    </span>
                  </div>
                  <p className="text-xs text-gray-400">{evt.message}</p>
                </div>
              </div>
            ))
          )}
        </div>

        {/* Footer */}
        <div className="p-3 bg-[#161B22] border-t border-[#2D333B] text-center text-xs text-gray-400">
          دستگاه مجهز به ماژول SIM800 با حافظه ثبت وقایع آفلاین
        </div>
      </div>
    </div>
  );
}
''')

    # 4. ConfirmModal.jsx
    with open('/home/user/kdd-prototype/src/components/ConfirmModal.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React from 'react';
import { AlertTriangle, ShieldCheck, X } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function ConfirmModal({ isOpen, onClose, onConfirm, title, message, confirmText = 'تأیید و اجرا', isDangerous = false }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-md">
      <div className="w-full max-w-xs bg-[#161B22] border border-[#2D333B] rounded-2xl p-5 shadow-2xl text-center animate-scaleUp">
        <div className={`w-12 h-12 mx-auto mb-3 rounded-full flex items-center justify-center ${
          isDangerous ? 'bg-red-500/20 text-red-500 shadow-[0_0_20px_rgba(239,68,68,0.3)]' : 'bg-[#1F6BFF]/20 text-[#1F6BFF] shadow-[0_0_20px_rgba(31,107,255,0.3)]'
        }`}>
          {isDangerous ? <AlertTriangle className="w-6 h-6" /> : <ShieldCheck className="w-6 h-6" />}
        </div>

        <h3 className="text-base font-bold text-gray-100 mb-2">{title}</h3>
        <p className="text-xs text-gray-400 leading-relaxed mb-5">{message}</p>

        <div className="flex gap-2">
          <button
            onClick={() => {
              playSound('click');
              onClose();
            }}
            className="flex-1 py-2.5 rounded-xl border border-[#2D333B] bg-[#0D1117] text-gray-300 text-xs font-semibold hover:bg-[#2D333B] transition-colors"
          >
            انصراف
          </button>
          <button
            onClick={() => {
              playSound(isDangerous ? 'alarm' : 'arm');
              onConfirm();
              onClose();
            }}
            className={`flex-1 py-2.5 rounded-xl text-white text-xs font-semibold shadow-lg transition-all ${
              isDangerous
                ? 'bg-red-600 hover:bg-red-500 shadow-red-600/30'
                : 'bg-[#1F6BFF] hover:bg-[#1A5BDB] shadow-[#1F6BFF]/40'
            }`}
          >
            {confirmText}
          </button>
        </div>
      </div>
    </div>
  );
}
''')

    print("Core components created successfully!")

create_components()
