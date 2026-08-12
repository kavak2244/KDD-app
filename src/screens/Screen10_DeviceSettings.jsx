import React, { useState } from 'react';
import { Save, ArrowRight, Zap, Battery, Globe, PhoneCall, Radio, Mic, Volume2, Clock, ShieldAlert, Trash2, RotateCcw, Check } from 'lucide-react';
import { playSound } from '../utils/audio';
import ConfirmModal from '../components/ConfirmModal';

export default function Screen10_DeviceSettings({ settings, onUpdateSettings, onBack, onSaveAll }) {
  const [localSettings, setLocalSettings] = useState(settings);
  const [confirmModalData, setConfirmModalData] = useState(null);
  const [sirenModalOpen, setSirenModalOpen] = useState(false);
  const [tempDuration, setTempDuration] = useState(localSettings.sirenDurationMinutes || 1);

  const toggleSetting = (key) => {
    playSound('click');
    setLocalSettings(prev => ({ ...prev, [key]: !prev[key] }));
  };

  const handleActionClick = (title, message) => {
    playSound('arm');
    setConfirmModalData({
      title,
      message,
      action: () => {},
    });
  };

  const handleDeleteDevice = () => {
    setConfirmModalData({
      title: 'حذف دستگاه از حساب کاربری',
      message: 'آیا از حذف این دزدگیر مطمئن هستید؟ با این کار تمام دسترسی‌ها و تاریخچه‌ها پاک خواهند شد.',
      isDangerous: true,
      action: () => {
        playSound('alarm');
        onBack();
      },
    });
  };

  const handleFactoryReset = () => {
    setConfirmModalData({
      title: 'بازگردانی به تنظیمات کارخانه (Factory Reset)',
      message: 'تمام تنظیمات سنسورها، ریموت‌ها و کدهای ذخیره شده در EEPROM ماژول به حالت پیش‌فرض برمی‌گردد.',
      isDangerous: true,
      action: () => {
        playSound('alarm');
      },
    });
  };

  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      {/* Header */}
      <div className="flex items-center justify-between mb-4 pt-1">
        <button
          onClick={() => {
            playSound('click');
            onBack();
          }}
          className="p-2 rounded-xl bg-[#161B22] border border-[#2D333B] text-gray-300 hover:text-white"
        >
          <ArrowRight className="w-4 h-4" />
        </button>

        <h2 className="text-base font-bold text-white">تنظیمات سخت‌افزاری دستگاه</h2>

        <button
          onClick={() => {
            playSound('arm');
            onUpdateSettings(localSettings);
            onSaveAll();
          }}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-[#1F6BFF] hover:bg-[#1A5BDB] text-white text-xs font-bold shadow-[0_0_12px_#1F6BFF]"
        >
          <Save className="w-3.5 h-3.5" />
          <span>ذخیره</span>
        </button>
      </div>

      {/* Settings Rows */}
      <div className="flex-1 space-y-2.5 overflow-y-auto pb-4">
        {/* SMS on Power Cut */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <div className="flex gap-1.5">
            <button
              onClick={() => toggleSetting('powerCutSms')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                localSettings.powerCutSms ? 'bg-[#1F6BFF] text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              فعال
            </button>
            <button
              onClick={() => toggleSetting('powerCutSms')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                !localSettings.powerCutSms ? 'bg-gray-700 text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              غیرفعال
            </button>
          </div>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">پیامک قطع برق ۲۴V</span>
            <Zap className="w-4 h-4 text-[#1F6BFF]" />
          </div>
        </div>

        {/* SMS Battery Test */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <div className="flex gap-1.5">
            <button
              onClick={() => toggleSetting('batteryTestSms')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                localSettings.batteryTestSms ? 'bg-[#1F6BFF] text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              فعال
            </button>
            <button
              onClick={() => toggleSetting('batteryTestSms')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                !localSettings.batteryTestSms ? 'bg-gray-700 text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              غیرفعال
            </button>
          </div>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">پیامک تست دوره‌ای باتری</span>
            <Battery className="w-4 h-4 text-emerald-400" />
          </div>
        </div>

        {/* Device Language */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <div className="flex gap-1.5">
            <button
              onClick={() => setLocalSettings({ ...localSettings, language: 'فارسی' })}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                localSettings.language === 'فارسی' ? 'bg-[#1F6BFF] text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              فارسی
            </button>
            <button
              onClick={() => setLocalSettings({ ...localSettings, language: 'انگلیسی' })}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                localSettings.language === 'انگلیسی' ? 'bg-[#1F6BFF] text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              English
            </button>
          </div>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">زبان دستگاه و پیامک‌ها</span>
            <Globe className="w-4 h-4 text-[#1F6BFF]" />
          </div>
        </div>

        {/* Call on Power Cut */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <div className="flex gap-1.5">
            <button
              onClick={() => toggleSetting('callOnPowerCut')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                localSettings.callOnPowerCut ? 'bg-[#1F6BFF] text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              فعال
            </button>
            <button
              onClick={() => toggleSetting('callOnPowerCut')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                !localSettings.callOnPowerCut ? 'bg-gray-700 text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              غیرفعال
            </button>
          </div>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">تماس خودکار در قطعی برق</span>
            <PhoneCall className="w-4 h-4 text-blue-400" />
          </div>
        </div>

        {/* Remote Semi-arm Mode */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <div className="flex gap-1.5">
            <button
              onClick={() => toggleSetting('remoteSemiArm')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                localSettings.remoteSemiArm ? 'bg-[#1F6BFF] text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              فعال
            </button>
            <button
              onClick={() => toggleSetting('remoteSemiArm')}
              className={`px-3 py-1 rounded-xl text-xs font-bold transition-all ${
                !localSettings.remoteSemiArm ? 'bg-gray-700 text-white' : 'bg-[#0D1117] text-gray-400 border border-[#2D333B]'
              }`}
            >
              غیرفعال
            </button>
          </div>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">حالت نیمه‌فعال ریموت</span>
            <Radio className="w-4 h-4 text-[#1F6BFF]" />
          </div>
        </div>

        {/* Remote learn trigger */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <button
            onClick={() => handleActionClick('افزودن ریموت از راه دور', 'فرمان آماده‌سازی لرن ریموت به سخت‌افزار ارسال شد. دکمه ریموت را فشار دهید.')}
            className="px-3.5 py-1.5 rounded-xl bg-[#0D1117] border border-[#1F6BFF]/40 text-[#1F6BFF] hover:bg-[#1F6BFF] hover:text-white text-xs font-bold transition-all"
          >
            اعمال
          </button>
          <span className="text-xs font-semibold text-gray-200">اضافه کردن ریموت از راه دور</span>
        </div>

        {/* Wireless sensor learn trigger */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <button
            onClick={() => handleActionClick('افزودن سنسور بی‌سیم', 'فرمان آماده‌سازی شناسه سنسور بی‌سیم به ماژول ارسال شد.')}
            className="px-3.5 py-1.5 rounded-xl bg-[#0D1117] border border-[#1F6BFF]/40 text-[#1F6BFF] hover:bg-[#1F6BFF] hover:text-white text-xs font-bold transition-all"
          >
            اعمال
          </button>
          <span className="text-xs font-semibold text-gray-200">اضافه کردن سنسور بی‌سیم از راه دور</span>
        </div>

        {/* Voice Record */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <button
            onClick={() => handleActionClick('ضبط صدا در دستگاه', 'دستگاه آماده ضبط صدای هشدار به مدت ۲۰ ثانیه می‌باشد.')}
            className="px-3.5 py-1.5 rounded-xl bg-[#0D1117] border border-[#1F6BFF]/40 text-[#1F6BFF] hover:bg-[#1F6BFF] hover:text-white text-xs font-bold transition-all"
          >
            اعمال
          </button>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">ضبط صدا روی حافظه برد</span>
            <Mic className="w-4 h-4 text-rose-400" />
          </div>
        </div>

        {/* Speaker Melody */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <select
            value={localSettings.speakerMelody}
            onChange={(e) => setLocalSettings({ ...localSettings, speakerMelody: e.target.value })}
            className="bg-[#0D1117] border border-[#2D333B] rounded-xl px-3 py-1.5 text-xs text-white outline-none"
          >
            <option value="ملودی ۱">ملودی ۱ (کلاسیک)</option>
            <option value="ملودی ۲">ملودی ۲ (مدرن)</option>
            <option value="ملودی ۳">ملودی ۳ (صنعتی)</option>
            <option value="ملودی ۴">ملودی ۴ (پالس سریع)</option>
          </select>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">ملودی اسپیکر و آژیر</span>
            <Volume2 className="w-4 h-4 text-amber-400" />
          </div>
        </div>

        {/* Siren Duration */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <button
            onClick={() => setSirenModalOpen(true)}
            className="px-3 py-1.5 rounded-xl bg-[#0D1117] border border-[#2D333B] text-xs text-gray-300 hover:text-white flex items-center gap-1.5"
          >
            <span>ویرایش ({localSettings.sirenDurationMinutes} دقیقه)</span>
          </button>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">مدت زمان فعال ماندن آژیر</span>
            <Clock className="w-4 h-4 text-[#1F6BFF]" />
          </div>
        </div>

        {/* Alarm Mode */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <select
            value={localSettings.alarmMode}
            onChange={(e) => setLocalSettings({ ...localSettings, alarmMode: e.target.value })}
            className="bg-[#0D1117] border border-[#2D333B] rounded-xl px-2 py-1.5 text-xs text-white outline-none max-w-[190px]"
          >
            <option value="ابتدا تماس سپس پیامک با تکرار">تماس ➔ پیامک با تکرار</option>
            <option value="پیامک و تماس همزمان">پیامک و تماس همزمان</option>
            <option value="فقط پیامک اضطراری">فقط پیامک اضطراری</option>
          </select>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-200">مُد آلارم اضطراری</span>
            <ShieldAlert className="w-4 h-4 text-red-400" />
          </div>
        </div>

        {/* Delete Device Button */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-red-500/30 flex items-center justify-between">
          <button
            onClick={handleDeleteDevice}
            className="px-3.5 py-1.5 rounded-xl bg-red-600/20 text-red-400 hover:bg-red-600 hover:text-white border border-red-500/40 text-xs font-bold transition-all"
          >
            اعمال حذف
          </button>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-red-400">حذف دستگاه از نرم‌افزار</span>
            <Trash2 className="w-4 h-4 text-red-400" />
          </div>
        </div>

        {/* Factory Reset */}
        <div className="p-3 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <button
            onClick={handleFactoryReset}
            className="px-3.5 py-1.5 rounded-xl bg-[#0D1117] border border-[#2D333B] text-gray-400 hover:text-amber-400 text-xs font-bold transition-all"
          >
            بازگردانی
          </button>
          <div className="flex items-center gap-2 text-right">
            <span className="text-xs font-semibold text-gray-300">بازگردانی به تنظیمات اولیه کارخانه</span>
            <RotateCcw className="w-4 h-4 text-gray-400" />
          </div>
        </div>
      </div>

      {/* Siren duration modal */}
      {sirenModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-sm">
          <div className="w-full max-w-xs bg-[#161B22] border border-[#2D333B] rounded-2xl p-4 text-right">
            <h3 className="text-sm font-bold text-white mb-2">تعیین مدت زمان آژیر</h3>
            <p className="text-xs text-gray-400 mb-4">مدت فعال ماندن خروجی آژیر پس از هر بار تحریک سنسورها:</p>
            <div className="flex items-center justify-center gap-3 mb-5">
              <span className="text-2xl font-black text-[#1F6BFF] font-mono">{tempDuration}</span>
              <span className="text-sm text-gray-300">دقیقه</span>
            </div>
            <input
              type="range"
              min="1"
              max="10"
              value={tempDuration}
              onChange={(e) => setTempDuration(Number(e.target.value))}
              className="w-full mb-5 accent-[#1F6BFF]"
            />
            <div className="flex gap-2">
              <button
                onClick={() => setSirenModalOpen(false)}
                className="flex-1 py-2 rounded-xl bg-[#0D1117] border border-[#2D333B] text-xs text-gray-300"
              >
                انصراف
              </button>
              <button
                onClick={() => {
                  setLocalSettings({ ...localSettings, sirenDurationMinutes: tempDuration });
                  setSirenModalOpen(false);
                }}
                className="flex-1 py-2 rounded-xl bg-[#1F6BFF] text-xs text-white font-bold"
              >
                تأیید
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
