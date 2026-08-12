import React, { useState, useEffect, useRef } from 'react';
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
