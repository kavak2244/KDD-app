import React, { useState } from 'react';
import { ArrowRight, Save, Radio, Edit2, CheckCircle2, ShieldAlert, Activity, RefreshCw } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen14_Sensors({
  sensors,
  onChangePartition,
  onToggleType,
  onToggle24h,
  onTriggerSensor,
  onBack,
  onSaveAll
}) {
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

        <h2 className="text-base font-bold text-white">مدیریت سنسورها (زون‌ها)</h2>

        <button
          onClick={handleSave}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-[#1F6BFF] hover:bg-[#1A5BDB] text-white text-xs font-bold shadow-[0_0_12px_#1F6BFF]"
        >
          <Save className="w-3.5 h-3.5" />
          <span>ذخیره</span>
        </button>
      </div>

      {savedSuccess && (
        <div className="mb-2 p-2 rounded-xl bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-xs flex items-center justify-center gap-2">
          <CheckCircle2 className="w-4 h-4" />
          <span>تنظیمات سنسورها با موفقیت در EEPROM ذخیره شد</span>
        </div>
      )}

      {/* Action Header Tabs */}
      <div className="grid grid-cols-2 gap-2 mb-3">
        <button
          onClick={() => playSound('click')}
          className="py-1.5 px-2 rounded-xl bg-[#161B22] border border-[#2D333B] text-[11px] text-gray-300 hover:text-white flex items-center justify-center gap-1"
        >
          <RefreshCw className="w-3.5 h-3.5 text-[#1F6BFF]" />
          <span>استعلام زون‌های پارتیشن</span>
        </button>

        <button
          onClick={() => playSound('click')}
          className="py-1.5 px-2 rounded-xl bg-[#161B22] border border-[#2D333B] text-[11px] text-gray-300 hover:text-white flex items-center justify-center gap-1"
        >
          <Activity className="w-3.5 h-3.5 text-[#1F6BFF]" />
          <span>استعلام وضعیت سنسورها</span>
        </button>
      </div>

      {/* Sensors List */}
      <div className="flex-1 space-y-2.5 overflow-y-auto pb-4">
        {sensors.map((sensor) => (
          <div
            key={sensor.id}
            className={`p-3 rounded-2xl border transition-all ${
              sensor.isTriggered
                ? 'bg-red-950/20 border-red-500 shadow-[0_0_15px_rgba(239,68,68,0.3)]'
                : 'bg-[#161B22] border-[#2D333B]'
            }`}
          >
            {/* Header: Name + Trigger Test Button */}
            <div className="flex items-center justify-between mb-2">
              <button
                onClick={() => onTriggerSensor(sensor.id)}
                className={`px-2.5 py-1 rounded-lg text-[10px] font-bold transition-all ${
                  sensor.isTriggered
                    ? 'bg-red-600 text-white animate-pulse'
                    : 'bg-[#0D1117] text-gray-400 hover:text-red-400 border border-[#2D333B]'
                }`}
                title="تست واکنش دزدگیر به تحریک این سنسور"
              >
                {sensor.isTriggered ? 'هشدار فعال!' : 'تست تحریک'}
              </button>

              <div className="flex items-center gap-2">
                <span className="text-xs font-bold text-white">{sensor.name}</span>
                <span className="w-2 h-2 rounded-full bg-[#1F6BFF]" />
              </div>
            </div>

            {/* Row with Partition + Mode NO/NC + 24H */}
            <div className="grid grid-cols-3 gap-2 pt-2 border-t border-[#2D333B]/60 text-xs">
              {/* 24-Hour Toggle */}
              <div className="flex items-center justify-between bg-[#0D1117] p-1.5 rounded-xl border border-[#2D333B]">
                <button
                  type="button"
                  onClick={() => onToggle24h(sensor.id)}
                  className={`w-8 h-4 rounded-full transition-colors relative p-0.5 ${
                    sensor.is24h ? 'bg-[#1F6BFF]' : 'bg-gray-700'
                  }`}
                >
                  <div className={`w-3 h-3 rounded-full bg-white transition-transform ${
                    sensor.is24h ? '-translate-x-4' : 'translate-x-0'
                  }`} />
                </button>
                <span className="text-[10px] text-gray-300">۲۴ ساعته</span>
              </div>

              {/* Mode NO / NC */}
              <div className="flex items-center justify-between bg-[#0D1117] p-1.5 rounded-xl border border-[#2D333B]">
                <select
                  value={sensor.type}
                  onChange={(e) => onToggleType(sensor.id, e.target.value)}
                  className="bg-transparent text-xs text-[#1F6BFF] font-bold outline-none cursor-pointer"
                >
                  <option value="NO">NO</option>
                  <option value="NC">NC</option>
                </select>
                <span className="text-[10px] text-gray-400">حالت:</span>
              </div>

              {/* Partition */}
              <div className="flex items-center justify-between bg-[#0D1117] p-1.5 rounded-xl border border-[#2D333B]">
                <select
                  value={sensor.partition}
                  onChange={(e) => onChangePartition(sensor.id, Number(e.target.value))}
                  className="bg-transparent text-xs text-white font-bold outline-none cursor-pointer"
                >
                  <option value={1}>۱</option>
                  <option value={2}>۲</option>
                  <option value={3}>۳</option>
                  <option value={4}>۴</option>
                </select>
                <span className="text-[10px] text-gray-400">پارتیشن:</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
