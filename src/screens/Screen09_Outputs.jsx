import React, { useState } from 'react';
import { Zap, Power, Clock, Edit2, ShieldAlert, Check } from 'lucide-react';
import { playSound } from '../utils/audio';
import ConfirmModal from '../components/ConfirmModal';

export default function Screen09_Outputs({ relays, onToggleRelay, onPulseRelay, onRenameRelay, onChangeRelayMode }) {
  const [editingRelay, setEditingRelay] = useState(null);
  const [tempName, setTempName] = useState('');
  const [confirmModalData, setConfirmModalData] = useState(null);

  const handleToggleClick = (relay) => {
    if (relay.isCritical && !relay.state) {
      setConfirmModalData({
        title: `فعال‌سازی ${relay.name}`,
        message: 'این خروجی دارای اهمیت امنیتی بالا است (قطع‌کن استارت/سوخت یا پمپ). آیا از ارسال فرمان مطمئن هستید؟',
        isDangerous: true,
        action: () => onToggleRelay(relay.id),
      });
    } else {
      playSound('relay');
      onToggleRelay(relay.id);
    }
  };

  const handlePulseClick = (relay) => {
    playSound('relay');
    onPulseRelay(relay.id);
  };

  const handleSaveRename = () => {
    if (editingRelay && tempName.trim()) {
      onRenameRelay(editingRelay.id, tempName.trim());
      setEditingRelay(null);
    }
  };

  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      {/* Top Banner */}
      <div className="p-3.5 rounded-2xl bg-gradient-to-b from-[#161B22] to-[#12171F] border border-[#2D333B] flex items-center justify-between mb-4">
        <div className="w-10 h-10 rounded-xl bg-[#1F6BFF]/15 border border-[#1F6BFF]/30 text-[#1F6BFF] flex items-center justify-center">
          <Zap className="w-5 h-5" />
        </div>
        <div className="text-right">
          <h2 className="text-base font-bold text-white mb-0.5">مدیریت خروجی‌های رله</h2>
          <p className="text-xs text-gray-400">کنترل، تغییر نام و زمان‌بندی ۸ رله سخت‌افزاری</p>
        </div>
      </div>

      {/* Relays List */}
      <div className="flex-1 space-y-2.5 overflow-y-auto pb-4">
        {relays.map((relay) => (
          <div
            key={relay.id}
            className={`p-3 rounded-2xl border transition-all ${
              relay.state
                ? 'bg-[#161B22] border-[#1F6BFF] shadow-[0_0_15px_rgba(31,107,255,0.2)]'
                : 'bg-[#161B22] border-[#2D333B]'
            }`}
          >
            {/* Header: Name + Edit */}
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center gap-1.5">
                <button
                  onClick={() => {
                    setEditingRelay(relay);
                    setTempName(relay.name);
                  }}
                  className="p-1 rounded-lg text-gray-400 hover:text-white hover:bg-[#2D333B]"
                  title="تغییر نام خروجی"
                >
                  <Edit2 className="w-3.5 h-3.5" />
                </button>
                <select
                  value={relay.mode}
                  onChange={(e) => onChangeRelayMode(relay.id, e.target.value)}
                  className="bg-[#0D1117] border border-[#2D333B] rounded-lg px-2 py-0.5 text-[11px] text-gray-300 outline-none"
                >
                  <option value="مستقل">مستقل</option>
                  <option value="پارتیشن ۱">پارتیشن ۱</option>
                  <option value="پارتیشن ۲">پارتیشن ۲</option>
                  <option value="اتوماتیک">اتوماتیک</option>
                </select>
              </div>

              <div className="flex items-center gap-2">
                <span className="text-xs font-bold text-white">خروجی {relay.id} — {relay.name}</span>
                {relay.isCritical && (
                  <span className="w-2 h-2 rounded-full bg-red-500 shadow-[0_0_6px_#EF4444]" title="خروجی حساس" />
                )}
              </div>
            </div>

            {/* Action Segmented Controls */}
            <div className="grid grid-cols-3 gap-2">
              <button
                onClick={() => handleToggleClick(relay)}
                className={`py-1.5 rounded-xl text-xs font-semibold flex items-center justify-center gap-1 transition-all ${
                  !relay.state
                    ? 'bg-gray-700/60 text-white border border-gray-500'
                    : 'bg-[#0D1117] text-gray-400 hover:text-white border border-[#2D333B]'
                }`}
              >
                <Power className="w-3.5 h-3.5" />
                <span>خاموش</span>
              </button>

              <button
                onClick={() => handleToggleClick(relay)}
                className={`py-1.5 rounded-xl text-xs font-semibold flex items-center justify-center gap-1 transition-all ${
                  relay.state
                    ? 'bg-[#1F6BFF] text-white shadow-[0_0_12px_#1F6BFF]'
                    : 'bg-[#0D1117] text-gray-400 hover:text-white border border-[#2D333B]'
                }`}
              >
                <Zap className="w-3.5 h-3.5" />
                <span>روشن</span>
              </button>

              <button
                onClick={() => handlePulseClick(relay)}
                className="py-1.5 rounded-xl bg-[#0D1117] text-gray-400 hover:text-[#1F6BFF] hover:border-[#1F6BFF] border border-[#2D333B] text-xs font-semibold flex items-center justify-center gap-1 transition-all"
              >
                <Clock className="w-3.5 h-3.5" />
                <span>لحظه‌ای</span>
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* Rename Modal */}
      {editingRelay && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-sm">
          <div className="w-full max-w-xs bg-[#161B22] border border-[#2D333B] rounded-2xl p-4 text-right">
            <h3 className="text-sm font-bold text-white mb-2">تغییر نام خروجی {editingRelay.id}</h3>
            <input
              type="text"
              value={tempName}
              onChange={(e) => setTempName(e.target.value)}
              className="w-full bg-[#0D1117] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3 py-2 text-xs text-white outline-none mb-4"
              placeholder="نام جدید رله..."
            />
            <div className="flex gap-2">
              <button
                onClick={() => setEditingRelay(null)}
                className="flex-1 py-2 rounded-xl bg-[#0D1117] border border-[#2D333B] text-xs text-gray-300"
              >
                انصراف
              </button>
              <button
                onClick={handleSaveRename}
                className="flex-1 py-2 rounded-xl bg-[#1F6BFF] text-xs text-white font-bold"
              >
                ذخیره نام
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Confirm Modal */}
      <ConfirmModal
        isOpen={!!confirmModalData}
        onClose={() => setConfirmModalData(null)}
        onConfirm={confirmModalData?.action || (() => {})}
        title={confirmModalData?.title || ''}
        message={confirmModalData?.message || ''}
        isDangerous={confirmModalData?.isDangerous}
      />
    </div>
  );
}
