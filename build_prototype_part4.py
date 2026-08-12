import os

def create_screens_part4():
    # Screen 11: Remote Coding
    with open('/home/user/kdd-prototype/src/screens/Screen11_RemoteCoding.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState } from 'react';
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
''')

    # Screen 12: Remotes
    with open('/home/user/kdd-prototype/src/screens/Screen12_Remotes.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState } from 'react';
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
''')

    # Screen 13: Contacts
    with open('/home/user/kdd-prototype/src/screens/Screen13_Contacts.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState } from 'react';
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
''')

    # Screen 14: Sensors
    with open('/home/user/kdd-prototype/src/screens/Screen14_Sensors.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState } from 'react';
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
''')

    print("Screens 11-14 created successfully!")

create_screens_part4()
