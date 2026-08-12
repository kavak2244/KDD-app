import React, { useState } from 'react';
import { ArrowRight, QrCode, Smartphone, ChevronLeft, Check } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen03_RegisterStep1({ formData, setFormData, onNext, onBack }) {
  const [scanModalOpen, setScanModalOpen] = useState(false);

  const handleSimSelect = (simIndex) => {
    playSound('click');
    setFormData({ ...formData, activeSim: simIndex });
  };

  const handleSimulateScan = () => {
    playSound('arm');
    setFormData({
      ...formData,
      serial: 'KDD-FH500-' + Math.floor(1000 + Math.random() * 9000),
    });
    setScanModalOpen(false);
  };

  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      {/* Top Bar with Back button */}
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
        <h2 className="text-base font-bold text-white">ثبت دستگاه</h2>
        <div className="w-8" />
      </div>

      <p className="text-xs text-gray-400 mb-5 text-center">
        برای شروع، اطلاعات سخت‌افزاری و سیم‌کارت دستگاه را وارد کنید
      </p>

      {/* Stepper (3 Steps) */}
      <div className="flex items-center justify-between mb-6 px-4">
        {/* Step 3 */}
        <div className="flex flex-col items-center">
          <div className="w-7 h-7 rounded-full bg-[#161B22] border border-[#2D333B] text-gray-500 flex items-center justify-center text-xs font-bold mb-1">
            ۳
          </div>
          <span className="text-[10px] text-gray-500">تعیین رمز</span>
        </div>
        <div className="flex-1 h-0.5 bg-[#2D333B] mx-2" />

        {/* Step 2 */}
        <div className="flex flex-col items-center">
          <div className="w-7 h-7 rounded-full bg-[#161B22] border border-[#2D333B] text-gray-500 flex items-center justify-center text-xs font-bold mb-1">
            ۲
          </div>
          <span className="text-[10px] text-gray-500">اطلاعات گارانتی</span>
        </div>
        <div className="flex-1 h-0.5 bg-[#2D333B] mx-2" />

        {/* Step 1 (Active) */}
        <div className="flex flex-col items-center">
          <div className="w-7 h-7 rounded-full bg-[#1F6BFF] text-white flex items-center justify-center text-xs font-bold shadow-[0_0_12px_#1F6BFF] mb-1">
            ۱
          </div>
          <span className="text-[10px] text-[#1F6BFF] font-bold">ثبت دستگاه</span>
        </div>
      </div>

      {/* Form Fields */}
      <div className="flex-1 space-y-4 overflow-y-auto pb-4">
        {/* Field: Device Serial */}
        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1.5">
            شناسه دستگاه (Serial Number)
          </label>
          <div className="relative">
            <input
              type="text"
              dir="ltr"
              value={formData.serial || ''}
              onChange={(e) => setFormData({ ...formData, serial: e.target.value })}
              placeholder="KDD-FH500-0012"
              className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3.5 py-3 text-sm text-white font-mono placeholder:text-gray-600 outline-none transition-colors"
            />
            <button
              onClick={() => setScanModalOpen(true)}
              type="button"
              className="absolute left-2.5 top-1/2 -translate-y-1/2 p-1.5 rounded-lg bg-[#0D1117] border border-[#2D333B] text-[#1F6BFF] hover:bg-[#1F6BFF] hover:text-white transition-colors"
              title="اسکن بارکد دستگاه"
            >
              <QrCode className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Field: Device Name */}
        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1.5">
            نام دلخواه دستگاه / خودرو
          </label>
          <input
            type="text"
            value={formData.name || ''}
            onChange={(e) => setFormData({ ...formData, name: e.target.value })}
            placeholder="مثال: کامیون شماره ۱ (ولوو)"
            className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3.5 py-3 text-sm text-white placeholder:text-gray-600 outline-none transition-colors text-right"
          />
        </div>

        {/* Field: SIM Card Number */}
        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1.5">
            شماره سیم‌کارت دستگاه (SIM800)
          </label>
          <input
            type="tel"
            dir="ltr"
            value={formData.simNumber || ''}
            onChange={(e) => setFormData({ ...formData, simNumber: e.target.value })}
            placeholder="09123456789"
            className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3.5 py-3 text-sm text-white font-mono placeholder:text-gray-600 outline-none transition-colors"
          />
        </div>

        {/* Field: Active SIM Selector */}
        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1">
            انتخاب سیم‌کارت فعال در دستگاه
          </label>
          <p className="text-[11px] text-gray-500 mb-2">
            مشخص کنید ارتباط اولیه با دستگاه از طریق سیم ۱ یا سیم ۲ برقرار شود
          </p>
          <div className="grid grid-cols-2 gap-3">
            <button
              type="button"
              onClick={() => handleSimSelect(1)}
              className={`p-3 rounded-xl border flex items-center justify-between transition-all ${
                formData.activeSim === 1
                  ? 'bg-[#1F6BFF]/15 border-[#1F6BFF] text-white shadow-[0_0_15px_rgba(31,107,255,0.2)]'
                  : 'bg-[#161B22] border-[#2D333B] text-gray-400 hover:border-gray-600'
              }`}
            >
              <div className={`w-4 h-4 rounded-full border flex items-center justify-center ${
                formData.activeSim === 1 ? 'border-[#1F6BFF] bg-[#1F6BFF]' : 'border-gray-500'
              }`}>
                {formData.activeSim === 1 && <div className="w-1.5 h-1.5 rounded-full bg-white" />}
              </div>
              <span className="text-xs font-semibold">سیم‌کارت ۱</span>
            </button>

            <button
              type="button"
              onClick={() => handleSimSelect(2)}
              className={`p-3 rounded-xl border flex items-center justify-between transition-all ${
                formData.activeSim === 2
                  ? 'bg-[#1F6BFF]/15 border-[#1F6BFF] text-white shadow-[0_0_15px_rgba(31,107,255,0.2)]'
                  : 'bg-[#161B22] border-[#2D333B] text-gray-400 hover:border-gray-600'
              }`}
            >
              <div className={`w-4 h-4 rounded-full border flex items-center justify-center ${
                formData.activeSim === 2 ? 'border-[#1F6BFF] bg-[#1F6BFF]' : 'border-gray-500'
              }`}>
                {formData.activeSim === 2 && <div className="w-1.5 h-1.5 rounded-full bg-white" />}
              </div>
              <span className="text-xs font-semibold">سیم‌کارت ۲</span>
            </button>
          </div>
        </div>
      </div>

      {/* Next Button */}
      <div className="pt-3">
        <button
          onClick={() => {
            playSound('click');
            onNext();
          }}
          className="w-full py-3.5 px-6 rounded-2xl bg-[#1F6BFF] hover:bg-[#1A5BDB] text-white font-bold text-sm shadow-[0_0_20px_rgba(31,107,255,0.4)] transition-all flex items-center justify-center gap-2"
        >
          <span>ثبت و ادامه</span>
          <ChevronLeft className="w-4 h-4" />
        </button>
      </div>

      {/* Simulated QR Scanner Modal */}
      {scanModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md">
          <div className="w-full max-w-xs bg-[#161B22] border border-[#2D333B] rounded-2xl p-5 text-center">
            <h3 className="text-sm font-bold text-white mb-2">اسکنر بارکد سخت‌افزار KDD</h3>
            <p className="text-xs text-gray-400 mb-4">
              دوربین را روی برچسب بارکد پشت جعبه یا برد دستگاه نگه دارید
            </p>
            <div className="w-44 h-44 mx-auto border-2 border-dashed border-[#1F6BFF] rounded-xl flex items-center justify-center relative overflow-hidden bg-black/40 mb-4">
              <div className="absolute inset-x-0 h-0.5 bg-[#1F6BFF] shadow-[0_0_10px_#1F6BFF] kdd-laser-scanner" />
              <QrCode className="w-16 h-16 text-gray-600" />
            </div>
            <div className="flex gap-2">
              <button
                onClick={() => setScanModalOpen(false)}
                className="flex-1 py-2 rounded-xl bg-[#0D1117] border border-[#2D333B] text-xs text-gray-300"
              >
                انصراف
              </button>
              <button
                onClick={handleSimulateScan}
                className="flex-1 py-2 rounded-xl bg-[#1F6BFF] text-xs text-white font-bold"
              >
                تأیید اسکن
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
