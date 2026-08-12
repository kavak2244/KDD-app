import React from 'react';
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
