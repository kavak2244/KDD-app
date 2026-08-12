import React, { useState } from 'react';
import { ArrowRight, Save, Plus, Trash2, Phone, MessageSquare, Zap, Shield, FileText, CheckCircle2, UserCheck } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen13_Contacts({ contacts, onTogglePermission, onAddContact, onDeleteContact, onBack, onSaveAll }) {
  const [newContactModal, setNewContactModal] = useState(false);
  const [newContact, setNewContact] = useState({ name: '', phone: '', partition: 1 });
  const [savedSuccess, setSavedSuccess] = useState(false);

  const handleSave = () => {
    playSound('arm');
    setSavedSuccess(true);
    onSaveAll();
    setTimeout(() => setSavedSuccess(false), 2000);
  };

  const handleAddNew = () => {
    if (newContact.name.trim() && newContact.phone.trim()) {
      playSound('click');
      onAddContact(newContact);
      setNewContact({ name: '', phone: '', partition: 1 });
      setNewContactModal(false);
    }
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

        <h2 className="text-base font-bold text-white">مدیریت مخاطبین دستگاه</h2>

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
          <span>لیست مخاطبین و دسترسی‌ها به SIM800 ارسال شد</span>
        </div>
      )}

      {/* Top Action Tabs */}
      <div className="grid grid-cols-3 gap-2 mb-3">
        <button
          onClick={() => playSound('click')}
          className="py-1.5 px-2 rounded-xl bg-[#161B22] border border-[#2D333B] text-[11px] text-gray-300 hover:text-white text-center"
        >
          استعلام مخاطبین
        </button>
        <button
          onClick={() => playSound('click')}
          className="py-1.5 px-2 rounded-xl bg-[#1F6BFF]/20 border border-[#1F6BFF]/40 text-[11px] text-[#1F6BFF] font-bold text-center"
        >
          ثبت پارتیشن
        </button>
        <button
          onClick={() => playSound('click')}
          className="py-1.5 px-2 rounded-xl bg-[#161B22] border border-[#2D333B] text-[11px] text-gray-300 hover:text-white text-center"
        >
          استعلام وضعیت
        </button>
      </div>

      {/* Contacts List */}
      <div className="flex-1 space-y-3 overflow-y-auto pb-4">
        {contacts.map((c) => (
          <div
            key={c.id}
            className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] space-y-2.5"
          >
            {/* Top row: Index, Name, Phone, Delete */}
            <div className="flex items-center justify-between">
              <button
                onClick={() => {
                  playSound('click');
                  onDeleteContact(c.id);
                }}
                className="p-1 rounded-lg text-gray-500 hover:text-red-400 hover:bg-[#2D333B]"
                title="حذف مخاطب"
              >
                <Trash2 className="w-3.5 h-3.5" />
              </button>

              <div className="flex items-center gap-2">
                <span className="text-xs text-gray-400 font-mono" dir="ltr">{c.phone}</span>
                <span className="text-xs font-bold text-white">{c.name}</span>
                <div className="w-5 h-5 rounded-full bg-[#1F6BFF]/20 text-[#1F6BFF] flex items-center justify-center text-[10px] font-mono font-bold">
                  {c.id}
                </div>
              </div>
            </div>

            {/* Permission Checkbox Matrix */}
            <div className="grid grid-cols-3 gap-1.5 pt-2 border-t border-[#2D333B]/60 text-[10px]">
              {/* Call */}
              <label className="flex items-center justify-end gap-1.5 cursor-pointer bg-[#0D1117] p-1.5 rounded-lg border border-[#2D333B]">
                <span className="text-gray-300">تماس</span>
                <input
                  type="checkbox"
                  checked={c.call}
                  onChange={() => onTogglePermission(c.id, 'call')}
                  className="accent-[#1F6BFF] rounded"
                />
              </label>

              {/* SMS */}
              <label className="flex items-center justify-end gap-1.5 cursor-pointer bg-[#0D1117] p-1.5 rounded-lg border border-[#2D333B]">
                <span className="text-gray-300">پیامک</span>
                <input
                  type="checkbox"
                  checked={c.sms}
                  onChange={() => onTogglePermission(c.id, 'sms')}
                  className="accent-[#1F6BFF] rounded"
                />
              </label>

              {/* Power Cut */}
              <label className="flex items-center justify-end gap-1.5 cursor-pointer bg-[#0D1117] p-1.5 rounded-lg border border-[#2D333B]">
                <span className="text-gray-300">قطع برق</span>
                <input
                  type="checkbox"
                  checked={c.powerCut}
                  onChange={() => onTogglePermission(c.id, 'powerCut')}
                  className="accent-[#1F6BFF] rounded"
                />
              </label>

              {/* Arm / Disarm */}
              <label className="flex items-center justify-end gap-1.5 cursor-pointer bg-[#0D1117] p-1.5 rounded-lg border border-[#2D333B]">
                <span className="text-gray-300">فعال/غیرفعال</span>
                <input
                  type="checkbox"
                  checked={c.armDisarm}
                  onChange={() => onTogglePermission(c.id, 'armDisarm')}
                  className="accent-[#1F6BFF] rounded"
                />
              </label>

              {/* Reports */}
              <label className="flex items-center justify-end gap-1.5 cursor-pointer bg-[#0D1117] p-1.5 rounded-lg border border-[#2D333B]">
                <span className="text-gray-300">گزارش‌گیری</span>
                <input
                  type="checkbox"
                  checked={c.report}
                  onChange={() => onTogglePermission(c.id, 'report')}
                  className="accent-[#1F6BFF] rounded"
                />
              </label>

              {/* Admin */}
              <label className="flex items-center justify-end gap-1.5 cursor-pointer bg-[#0D1117] p-1.5 rounded-lg border border-[#2D333B]">
                <span className="text-amber-300 font-bold">مدیر</span>
                <input
                  type="checkbox"
                  checked={c.isAdmin}
                  onChange={() => onTogglePermission(c.id, 'isAdmin')}
                  className="accent-amber-500 rounded"
                />
              </label>
            </div>
          </div>
        ))}

        {/* Add Contact Button */}
        <button
          onClick={() => setNewContactModal(true)}
          className="w-full py-3 rounded-2xl border-2 border-dashed border-[#2D333B] hover:border-[#1F6BFF] text-gray-300 hover:text-white bg-[#161B22]/40 text-xs font-bold flex items-center justify-center gap-2"
        >
          <Plus className="w-4 h-4 text-[#1F6BFF]" />
          <span>افزودن مخاطب جدید</span>
        </button>
      </div>

      {/* Add Modal */}
      {newContactModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm">
          <div className="w-full max-w-xs bg-[#161B22] border border-[#2D333B] rounded-2xl p-4 text-right">
            <h3 className="text-sm font-bold text-white mb-3">افزودن مخاطب جدید</h3>
            
            <div className="space-y-3 mb-4">
              <div>
                <label className="block text-[11px] text-gray-300 mb-1">نام مخاطب:</label>
                <input
                  type="text"
                  value={newContact.name}
                  onChange={(e) => setNewContact({ ...newContact, name: e.target.value })}
                  placeholder="مثال: راننده شیفت شب"
                  className="w-full bg-[#0D1117] border border-[#2D333B] rounded-xl px-3 py-2 text-xs text-white outline-none"
                />
              </div>

              <div>
                <label className="block text-[11px] text-gray-300 mb-1">شماره تلفن همراه:</label>
                <input
                  type="tel"
                  dir="ltr"
                  value={newContact.phone}
                  onChange={(e) => setNewContact({ ...newContact, phone: e.target.value })}
                  placeholder="0912..."
                  className="w-full bg-[#0D1117] border border-[#2D333B] rounded-xl px-3 py-2 text-xs text-white font-mono outline-none"
                />
              </div>
            </div>

            <div className="flex gap-2">
              <button
                onClick={() => setNewContactModal(false)}
                className="flex-1 py-2 rounded-xl bg-[#0D1117] border border-[#2D333B] text-xs text-gray-300"
              >
                انصراف
              </button>
              <button
                onClick={handleAddNew}
                className="flex-1 py-2 rounded-xl bg-[#1F6BFF] text-xs text-white font-bold"
              >
                افزودن
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
