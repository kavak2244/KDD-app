import React, { useState } from 'react';
import { ArrowRight, Save, Lock, Unlock, VolumeX, Lightbulb, Trash2, Plus, Info, CheckCircle2 } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen11_RemoteCoding({ onBack, onSaveCode }) {
  const [selectedRemote, setSelectedRemote] = useState('ریموت ۱');
  const [sequence, setSequence] = useState(['باز', 'باز', 'قفل', 'قفل']);
  const [pressedBtn, setPressedBtn] = useState(null);
  const [savedSuccess, setSavedSuccess] = useState(false);

  const handleKeyPress = (keyName) => {
    playSound('click');
    setPressedBtn(keyName);
    setTimeout(() => setPressedBtn(null), 250);
    
    if (sequence.length < 8) {
      setSequence([...sequence, keyName]);
    }
  };

  const handleClear = () => {
    playSound('click');
    setSequence([]);
  };

  const handleSave = () => {
    playSound('arm');
    setSavedSuccess(true);
    onSaveCode(selectedRemote, sequence);
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

        <h2 className="text-base font-bold text-white">کدگذاری ریموت</h2>

        <button
          onClick={handleSave}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-[#1F6BFF] hover:bg-[#1A5BDB] text-white text-xs font-bold shadow-[0_0_12px_#1F6BFF]"
        >
          <Save className="w-3.5 h-3.5" />
          <span>ذخیره</span>
        </button>
      </div>

      {savedSuccess && (
        <div className="mb-3 p-2.5 rounded-xl bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-xs flex items-center justify-center gap-2 animate-fadeIn">
          <CheckCircle2 className="w-4 h-4" />
          <span>کد ریموت با موفقیت در سخت‌افزار ثبت شد!</span>
        </div>
      )}

      {/* Select Remote & Current Status */}
      <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] mb-3 space-y-2">
        <div className="flex items-center justify-between">
          <select
            value={selectedRemote}
            onChange={(e) => setSelectedRemote(e.target.value)}
            className="bg-[#0D1117] border border-[#2D333B] rounded-xl px-3 py-1.5 text-xs text-white outline-none"
          >
            {[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].map((num) => (
              <option key={num} value={`ریموت ${num}`}>ریموت شماره {num}</option>
            ))}
          </select>
          <span className="text-xs font-semibold text-gray-300">انتخاب ریموت هدف:</span>
        </div>

        <p className="text-[11px] text-gray-400">
          برای تعریف کد، کلیدهای روی ریموت را به ترتیب فشار دهید تا توالی ثبت شود.
        </p>
      </div>

      {/* Physical Keyfob Graphic Simulator */}
      <div className="flex-1 flex flex-col items-center justify-center my-auto">
        <div className="w-48 bg-gradient-to-b from-[#2A2E35] via-[#1E2229] to-[#12151B] p-4 rounded-3xl border-2 border-[#3F4754] shadow-[0_15px_35px_rgba(0,0,0,0.8)] relative">
          {/* LED indicator */}
          <div className="w-2.5 h-2.5 rounded-full bg-blue-500 mx-auto mb-3 shadow-[0_0_8px_#1F6BFF] animate-pulse" />

          {/* 4 Physical Buttons */}
          <div className="grid grid-cols-2 gap-3 mb-3">
            {/* Unlock Button */}
            <button
              onClick={() => handleKeyPress('باز')}
              className={`p-3.5 rounded-2xl border flex flex-col items-center justify-center gap-1 transition-all ${
                pressedBtn === 'باز'
                  ? 'bg-[#1F6BFF] text-white border-white scale-95 shadow-[0_0_15px_#1F6BFF]'
                  : 'bg-[#161B22] border-[#383F4C] text-gray-200 hover:border-[#1F6BFF]'
              }`}
            >
              <Unlock className="w-5 h-5 text-blue-400" />
              <span className="text-[10px] font-bold">باز</span>
            </button>

            {/* Lock Button */}
            <button
              onClick={() => handleKeyPress('قفل')}
              className={`p-3.5 rounded-2xl border flex flex-col items-center justify-center gap-1 transition-all ${
                pressedBtn === 'قفل'
                  ? 'bg-[#1F6BFF] text-white border-white scale-95 shadow-[0_0_15px_#1F6BFF]'
                  : 'bg-[#161B22] border-[#383F4C] text-gray-200 hover:border-[#1F6BFF]'
              }`}
            >
              <Lock className="w-5 h-5 text-blue-400" />
              <span className="text-[10px] font-bold">قفل</span>
            </button>
          </div>

          <div className="space-y-2">
            {/* Mute Button */}
            <button
              onClick={() => handleKeyPress('بی‌صدا')}
              className={`w-full py-2.5 rounded-xl border flex items-center justify-center gap-1.5 transition-all ${
                pressedBtn === 'بی‌صدا'
                  ? 'bg-[#1F6BFF] text-white scale-95'
                  : 'bg-[#161B22] border-[#383F4C] text-gray-300 hover:border-gray-500'
              }`}
            >
              <VolumeX className="w-4 h-4" />
              <span className="text-[10px]">بی‌صدا</span>
            </button>

            {/* Light / Aux Button */}
            <button
              onClick={() => handleKeyPress('چراغ')}
              className={`w-full py-2.5 rounded-xl border flex items-center justify-center gap-1.5 transition-all ${
                pressedBtn === 'چراغ'
                  ? 'bg-[#1F6BFF] text-white scale-95'
                  : 'bg-[#161B22] border-[#383F4C] text-gray-300 hover:border-gray-500'
              }`}
            >
              <Lightbulb className="w-4 h-4 text-amber-400" />
              <span className="text-[10px]">چراغ / AUX</span>
            </button>
          </div>
        </div>
      </div>

      {/* Sequence Badges */}
      <div className="p-3.5 rounded-2xl bg-[#161B22] border border-[#2D333B] space-y-2 mt-auto">
        <div className="flex items-center justify-between">
          <button
            onClick={handleClear}
            className="flex items-center gap-1 text-[11px] text-red-400 hover:text-red-300"
          >
            <Trash2 className="w-3.5 h-3.5" />
            <span>پاک کردن توالی</span>
          </button>
          <span className="text-xs font-bold text-gray-300">توالی فشرده‌شده:</span>
        </div>

        {sequence.length === 0 ? (
          <div className="text-center py-2 text-xs text-gray-500 italic">
            روی کلیدهای ریموت بالا کلیک کنید...
          </div>
        ) : (
          <div className="flex items-center gap-2 overflow-x-auto py-1" dir="ltr">
            {sequence.map((key, idx) => (
              <div
                key={idx}
                className="px-3 py-1 rounded-xl bg-[#1F6BFF]/20 border border-[#1F6BFF]/50 text-white text-xs font-bold flex items-center gap-1.5 shrink-0 shadow-[0_0_10px_rgba(31,107,255,0.3)]"
              >
                <span className="text-[10px] text-gray-400 font-mono">{idx + 1}</span>
                <span>{key}</span>
              </div>
            ))}
          </div>
        )}

        {/* Quick Add Buttons */}
        <div className="grid grid-cols-2 gap-2 pt-1 border-t border-[#2D333B]/60">
          <button
            onClick={() => handleKeyPress('قفل')}
            className="py-2 rounded-xl bg-[#0D1117] border border-[#2D333B] text-gray-300 hover:text-white text-xs font-semibold flex items-center justify-center gap-1"
          >
            <Lock className="w-3.5 h-3.5 text-[#1F6BFF]" />
            <span>+ افزودن قفل</span>
          </button>
          <button
            onClick={() => handleKeyPress('باز')}
            className="py-2 rounded-xl bg-[#0D1117] border border-[#2D333B] text-gray-300 hover:text-white text-xs font-semibold flex items-center justify-center gap-1"
          >
            <Unlock className="w-3.5 h-3.5 text-[#1F6BFF]" />
            <span>+ افزودن باز</span>
          </button>
        </div>
      </div>
    </div>
  );
}
