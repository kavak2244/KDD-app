import React, { useState } from 'react';
import { ArrowRight, Save, Lock, Unlock, Edit2, Trash2, Cpu, CheckCircle2 } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen12_Remotes({ remotes, onToggleLockRemote, onChangePartition, onBack, onSaveAll }) {
  const [savedSuccess, setSavedSuccess] = useState(false);

  const handleSave = () => {
    playSound('arm');
    setSavedSuccess(true);
    onSaveAll();
    setTimeout(() => setSavedSuccess(false), 2000);
  };

  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      {/* Header */}
      <div className="flex items-center justify-between mb-3 pt-1">
        <button
          onClick={() => {
            playSound('click');
            onBack();
          }}
          className="p-2 rounded-xl bg-[#161B22] border border-[#2D333B] text-gray-300 hover:text-white"
        >
          <ArrowRight className="w-4 h-4" />
        </button>

        <h2 className="text-base font-bold text-white">مدیریت ریموت‌ها</h2>

        <button
          onClick={handleSave}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-[#1F6BFF] hover:bg-[#1A5BDB] text-white text-xs font-bold shadow-[0_0_12px_#1F6BFF]"
        >
          <Save className="w-3.5 h-3.5" />
          <span>ذخیره</span>
        </button>
      </div>

      {savedSuccess && (
        <div className="mb-3 p-2 rounded-xl bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-xs flex items-center justify-center gap-2">
          <CheckCircle2 className="w-4 h-4" />
          <span>تنظیمات ریموت‌ها با موفقیت ذخیره شد</span>
        </div>
      )}

      <p className="text-xs text-gray-400 mb-3">
        تعیین پارتیشن و قفل‌کردن ریموت‌های مفقودی یا سرقت‌شده (۱۰ ریموت سخت‌افزاری)
      </p>

      {/* Remotes 2-Column Grid */}
      <div className="flex-1 grid grid-cols-2 gap-2.5 overflow-y-auto pb-4">
        {remotes.map((remote) => (
          <div
            key={remote.id}
            className={`p-3 rounded-2xl border transition-all flex flex-col justify-between ${
              remote.isLocked
                ? 'bg-[#161B22]/50 border-red-500/30 opacity-75'
                : 'bg-[#161B22] border-[#2D333B] hover:border-gray-600'
            }`}
          >
            {/* Header: Number & Name */}
            <div>
              <div className="flex items-center justify-between mb-2">
                <div className="w-6 h-6 rounded-lg bg-[#1F6BFF]/20 text-[#1F6BFF] flex items-center justify-center text-xs font-mono font-bold">
                  {remote.id}
                </div>
                <span className="text-xs font-bold text-white truncate max-w-[90px]">
                  {remote.name}
                </span>
              </div>

              {/* Partition Select */}
              <div className="mb-3">
                <span className="text-[10px] text-gray-400 block mb-1">پارتیشن:</span>
                <select
                  value={remote.partition}
                  onChange={(e) => onChangePartition(remote.id, Number(e.target.value))}
                  className="w-full bg-[#0D1117] border border-[#2D333B] rounded-lg px-2 py-1 text-xs text-white outline-none"
                >
                  <option value={1}>پارتیشن ۱</option>
                  <option value={2}>پارتیشن ۲</option>
                  <option value={3}>پارتیشن ۳</option>
                  <option value={4}>پارتیشن ۴</option>
                </select>
              </div>
            </div>

            {/* Action buttons */}
            <div className="flex items-center justify-between pt-2 border-t border-[#2D333B]/60">
              <button
                onClick={() => {
                  playSound('click');
                  onToggleLockRemote(remote.id);
                }}
                className={`p-1.5 rounded-lg border text-xs transition-all ${
                  remote.isLocked
                    ? 'bg-red-500/20 text-red-400 border-red-500/40'
                    : 'bg-[#0D1117] text-gray-400 hover:text-white border-[#2D333B]'
                }`}
                title={remote.isLocked ? 'ریموت قفل است (غیرفعال)' : 'ریموت باز است (فعال)'}
              >
                {remote.isLocked ? <Lock className="w-3.5 h-3.5" /> : <Unlock className="w-3.5 h-3.5" />}
              </button>

              <span className={`text-[10px] font-semibold ${remote.isLocked ? 'text-red-400' : 'text-emerald-400'}`}>
                {remote.isLocked ? 'غیرفعال' : 'فعال'}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
