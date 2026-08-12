import React from 'react';
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
