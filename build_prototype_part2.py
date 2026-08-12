import os

def create_screens():
    # Screen 01: Splash
    with open('/home/user/kdd-prototype/src/screens/Screen01_Splash.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React from 'react';
import { Shield, ChevronLeft, Smartphone, Radio } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen01_Splash({ onStart, onRegister }) {
  return (
    <div className="min-h-full flex flex-col items-center justify-between p-6 bg-gradient-to-b from-[#0A0E17] via-[#0D1117] to-[#080B10] text-center relative overflow-hidden">
      {/* Background radial glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-80 h-80 bg-[#1F6BFF]/15 rounded-full blur-3xl pointer-events-none" />
      
      {/* Top spacing */}
      <div className="w-full pt-4 flex justify-between items-center text-xs text-gray-400">
        <span className="font-mono text-[#1F6BFF]">v1.2 Release</span>
        <div className="flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-[#161B22] border border-[#2D333B]">
          <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
          <span className="text-[11px] text-gray-300">SIM800 Ready</span>
        </div>
      </div>

      {/* Center Branding & Blue Energy Ring */}
      <div className="flex flex-col items-center my-auto">
        {/* Blue Energy Ring */}
        <div className="relative w-44 h-44 flex items-center justify-center mb-6">
          <div className="absolute inset-0 rounded-full border-2 border-[#1F6BFF]/30 kdd-energy-ring" />
          <div className="absolute inset-2 rounded-full border border-[#1F6BFF]/60 shadow-[0_0_35px_rgba(31,107,255,0.6)]" />
          
          {/* Logo Shield */}
          <div className="w-28 h-28 rounded-2xl bg-gradient-to-br from-[#1F6BFF]/30 to-[#161B22] border border-[#1F6BFF]/50 flex items-center justify-center shadow-2xl relative overflow-hidden backdrop-blur-md">
            <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-blue-400/20 via-transparent to-transparent" />
            <Shield className="w-14 h-14 text-white drop-shadow-[0_0_15px_#1F6BFF]" />
            <div className="absolute bottom-2 text-[10px] font-extrabold tracking-widest text-[#1F6BFF]">KDD</div>
          </div>
        </div>

        {/* Brand Slogan */}
        <h1 className="text-3xl font-black tracking-wider text-white mb-2">
          KDD <span className="text-[#1F6BFF] text-2xl font-light">SMART SECURITY</span>
        </h1>
        <p className="text-sm text-gray-300 font-medium tracking-wide">
          سامانه هوشمند حفاظت و ردیابی ماشین‌های سنگین
        </p>

        <div className="mt-4 flex items-center gap-2 text-xs text-gray-400 bg-[#161B22]/80 px-3 py-1.5 rounded-full border border-[#2D333B]">
          <Radio className="w-3.5 h-3.5 text-[#1F6BFF]" />
          <span>پشتیبانی دوگانه: اینترنت ابری + پیامک اضطراری</span>
        </div>
      </div>

      {/* Bottom Actions */}
      <div className="w-full space-y-3 pb-4">
        <button
          onClick={() => {
            playSound('arm');
            onStart();
          }}
          className="w-full py-3.5 px-6 rounded-2xl bg-[#1F6BFF] hover:bg-[#1A5BDB] text-white font-bold text-sm shadow-[0_0_25px_rgba(31,107,255,0.5)] transition-all flex items-center justify-center gap-2 group"
        >
          <span>ورود به داشبورد دستگاه‌ها</span>
          <ChevronLeft className="w-4 h-4 group-hover:-translate-x-1 transition-transform" />
        </button>

        <button
          onClick={() => {
            playSound('click');
            onRegister();
          }}
          className="w-full py-3 px-6 rounded-2xl bg-[#161B22] hover:bg-[#2D333B] text-gray-300 font-semibold text-xs border border-[#2D333B] transition-all flex items-center justify-center gap-2"
        >
          <Smartphone className="w-4 h-4 text-[#1F6BFF]" />
          <span>ثبت و راه‌اندازی دستگاه جدید (۳ مرحله)</span>
        </button>
      </div>
    </div>
  );
}
''')

    # Screen 02: My Devices
    with open('/home/user/kdd-prototype/src/screens/Screen02_MyDevices.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React from 'react';
import { Shield, ChevronLeft, Plus, Smartphone, Signal, Battery, CheckCircle2 } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen02_MyDevices({ devices, activeDeviceId, onSelectDevice, onAddNew }) {
  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117]">
      {/* Top Header */}
      <div className="mb-5 pt-2">
        <div className="flex items-center justify-between mb-1">
          <h2 className="text-xl font-bold text-white">دستگاه‌های من</h2>
          <span className="text-xs px-2.5 py-1 rounded-full bg-[#1F6BFF]/15 text-[#1F6BFF] font-semibold border border-[#1F6BFF]/30">
            {devices.length} خودرو متصل
          </span>
        </div>
        <p className="text-xs text-gray-400">
          برای کنترل و مشاهده وضعیت، یکی از ماشین‌ها را انتخاب کنید
        </p>
      </div>

      {/* Device Cards List */}
      <div className="flex-1 space-y-3 overflow-y-auto pb-4">
        {devices.map((dev) => {
          const isSelected = dev.id === activeDeviceId;
          return (
            <div
              key={dev.id}
              onClick={() => {
                playSound('click');
                onSelectDevice(dev.id);
              }}
              className={`p-4 rounded-2xl border transition-all cursor-pointer relative overflow-hidden ${
                isSelected
                  ? 'bg-gradient-to-r from-[#161B22] to-[#1a2332] border-[#1F6BFF] shadow-[0_0_20px_rgba(31,107,255,0.25)]'
                  : 'bg-[#161B22] border-[#2D333B] hover:border-gray-600'
              }`}
            >
              {/* Active Indicator bar */}
              {isSelected && (
                <div className="absolute top-0 right-0 left-0 h-1 bg-[#1F6BFF]" />
              )}

              <div className="flex items-center justify-between">
                {/* Left: Arrow & Armed Status */}
                <div className="flex items-center gap-2">
                  <ChevronLeft className="w-5 h-5 text-gray-400" />
                </div>

                {/* Center: Device Info */}
                <div className="flex-1 pr-3 text-right">
                  <div className="flex items-center justify-end gap-2 mb-1">
                    {isSelected && (
                      <span className="text-[10px] px-1.5 py-0.5 rounded bg-[#1F6BFF]/20 text-[#1F6BFF] font-semibold">
                        دستگاه فعال
                      </span>
                    )}
                    <h3 className="text-base font-bold text-white">{dev.name}</h3>
                  </div>

                  <div className="text-xs text-gray-400 font-mono flex items-center justify-end gap-2 mb-2">
                    <span>سریال: {dev.serial}</span>
                  </div>

                  {/* Status Badges */}
                  <div className="flex items-center justify-end gap-3 text-[11px] text-gray-400">
                    <span className="flex items-center gap-1">
                      <span className={`w-2 h-2 rounded-full ${dev.isArmed ? 'bg-emerald-400' : 'bg-blue-400'}`} />
                      {dev.isArmed ? 'حفاظت فعال' : 'آماده / غیرمسلح'}
                    </span>
                    <span className="flex items-center gap-1 font-mono">
                      <Battery className="w-3.5 h-3.5 text-emerald-400" />
                      {dev.battery}%
                    </span>
                    <span className="flex items-center gap-1">
                      <Signal className="w-3.5 h-3.5 text-blue-400" />
                      {dev.isOnline ? 'اینترنت' : 'SMS'}
                    </span>
                  </div>
                </div>

                {/* Right: Shield Icon */}
                <div className={`w-12 h-12 rounded-xl flex items-center justify-center border ${
                  dev.isArmed
                    ? 'bg-emerald-500/10 border-emerald-500/30 text-emerald-400'
                    : 'bg-[#1F6BFF]/10 border-[#1F6BFF]/30 text-[#1F6BFF]'
                }`}>
                  <Shield className="w-6 h-6" />
                </div>
              </div>
            </div>
          );
        })}

        {/* Add New Device Button */}
        <button
          onClick={() => {
            playSound('click');
            onAddNew();
          }}
          className="w-full p-4 rounded-2xl border-2 border-dashed border-[#2D333B] hover:border-[#1F6BFF] bg-[#161B22]/40 hover:bg-[#161B22] text-gray-300 hover:text-white transition-all flex items-center justify-center gap-2 group"
        >
          <div className="w-8 h-8 rounded-full bg-[#1F6BFF]/20 text-[#1F6BFF] flex items-center justify-center group-hover:scale-110 transition-transform">
            <Plus className="w-4 h-4" />
          </div>
          <span className="text-sm font-semibold">افزودن دستگاه و خودرو جدید</span>
        </button>
      </div>
    </div>
  );
}
''')

    # Screen 03: Register Step 1
    with open('/home/user/kdd-prototype/src/screens/Screen03_RegisterStep1.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState } from 'react';
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
''')

    # Screen 04: Register Step 2
    with open('/home/user/kdd-prototype/src/screens/Screen04_RegisterStep2.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React from 'react';
import { ArrowRight, ChevronLeft, Check, User, CreditCard, Phone, MapPin, Building, Wrench } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen04_RegisterStep2({ formData, setFormData, onNext, onBack }) {
  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      {/* Top Bar */}
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
        <h2 className="text-base font-bold text-white">ثبت گارانتی</h2>
        <div className="w-8" />
      </div>

      <p className="text-xs text-gray-400 mb-5 text-center">
        برای فعال‌سازی گارانتی و خدمات پس از فروش، اطلاعات زیر را تکمیل کنید
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
        <div className="flex-1 h-0.5 bg-[#1F6BFF] mx-2" />

        {/* Step 2 (Active) */}
        <div className="flex flex-col items-center">
          <div className="w-7 h-7 rounded-full bg-[#1F6BFF] text-white flex items-center justify-center text-xs font-bold shadow-[0_0_12px_#1F6BFF] mb-1">
            ۲
          </div>
          <span className="text-[10px] text-[#1F6BFF] font-bold">اطلاعات گارانتی</span>
        </div>
        <div className="flex-1 h-0.5 bg-[#1F6BFF] mx-2" />

        {/* Step 1 (Completed) */}
        <div className="flex flex-col items-center">
          <div className="w-7 h-7 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs font-bold mb-1">
            <Check className="w-4 h-4" />
          </div>
          <span className="text-[10px] text-emerald-400 font-medium">ثبت دستگاه</span>
        </div>
      </div>

      {/* Form Fields */}
      <div className="flex-1 space-y-3.5 overflow-y-auto pb-4">
        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1">
            نام و نام خانوادگی مالک
          </label>
          <input
            type="text"
            value={formData.ownerName || ''}
            onChange={(e) => setFormData({ ...formData, ownerName: e.target.value })}
            placeholder="مثال: علی احمدی"
            className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3.5 py-2.5 text-sm text-white placeholder:text-gray-600 outline-none transition-colors"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1">
            کد ملی مالک
          </label>
          <input
            type="text"
            dir="ltr"
            value={formData.nationalId || ''}
            onChange={(e) => setFormData({ ...formData, nationalId: e.target.value })}
            placeholder="0012345678"
            className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3.5 py-2.5 text-sm text-white font-mono placeholder:text-gray-600 outline-none transition-colors"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1">
            شماره تماس همراه مالک
          </label>
          <input
            type="tel"
            dir="ltr"
            value={formData.ownerPhone || ''}
            onChange={(e) => setFormData({ ...formData, ownerPhone: e.target.value })}
            placeholder="09123456789"
            className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3.5 py-2.5 text-sm text-white font-mono placeholder:text-gray-600 outline-none transition-colors"
          />
        </div>

        <div className="grid grid-cols-2 gap-3">
          <div>
            <label className="block text-xs font-semibold text-gray-300 mb-1">
              استان
            </label>
            <select
              value={formData.province || 'تهران'}
              onChange={(e) => setFormData({ ...formData, province: e.target.value })}
              className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3 py-2.5 text-xs text-white outline-none transition-colors"
            >
              <option value="تهران">تهران</option>
              <option value="اصفهان">اصفهان</option>
              <option value="فارس">فارس</option>
              <option value="خراسان رضوی">خراسان رضوی</option>
              <option value="آذربایجان شرقی">آذربایجان شرقی</option>
              <option value="خوزستان">خوزستان</option>
            </select>
          </div>

          <div>
            <label className="block text-xs font-semibold text-gray-300 mb-1">
              شهر
            </label>
            <input
              type="text"
              value={formData.city || ''}
              onChange={(e) => setFormData({ ...formData, city: e.target.value })}
              placeholder="مثال: تهران"
              className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3 py-2.5 text-xs text-white placeholder:text-gray-600 outline-none transition-colors"
            />
          </div>
        </div>

        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1">
            کد پستی ۱۰ رقمی
          </label>
          <input
            type="text"
            dir="ltr"
            value={formData.postalCode || ''}
            onChange={(e) => setFormData({ ...formData, postalCode: e.target.value })}
            placeholder="1234567890"
            className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3.5 py-2.5 text-sm text-white font-mono placeholder:text-gray-600 outline-none transition-colors"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1">
            نام تکنسین / نمایندگی مجاز نصب
          </label>
          <input
            type="text"
            value={formData.technician || ''}
            onChange={(e) => setFormData({ ...formData, technician: e.target.value })}
            placeholder="مثال: رضا محمدی (کد ۱۰۴)"
            className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3.5 py-2.5 text-sm text-white placeholder:text-gray-600 outline-none transition-colors"
          />
        </div>
      </div>

      {/* Sticky Primary Button */}
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
    </div>
  );
}
''')

    # Screen 05: Register Step 3
    with open('/home/user/kdd-prototype/src/screens/Screen05_RegisterStep3.jsx', 'w', encoding='utf-8') as f:
        f.write('''import React, { useState } from 'react';
import { ArrowRight, ChevronLeft, Check, Lock, Eye, EyeOff, Fingerprint, Info, ShieldCheck } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen05_RegisterStep3({ formData, setFormData, onComplete, onBack }) {
  const [showPass, setShowPass] = useState(false);
  const [showConfirmPass, setShowConfirmPass] = useState(false);

  const getPasswordStrength = (pass) => {
    if (!pass) return { score: 0, text: 'رمز وارد نشده', color: 'bg-gray-600' };
    if (pass.length < 4) return { score: 1, text: 'ضعیف', color: 'bg-red-500' };
    if (pass.length < 7) return { score: 2, text: 'متوسط', color: 'bg-[#1F6BFF]' };
    return { score: 4, text: 'قوی و امن', color: 'bg-emerald-500' };
  };

  const strength = getPasswordStrength(formData.password || '');

  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      {/* Top Bar */}
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
        <h2 className="text-base font-bold text-white">تعیین رمز عبور</h2>
        <div className="w-8" />
      </div>

      <p className="text-xs text-gray-400 mb-5 text-center">
        برای افزایش امنیت، یک رمز عبور برای ورود به اپلیکیشن و ارسال پیامک تعیین کنید
      </p>

      {/* Stepper (3 Steps) */}
      <div className="flex items-center justify-between mb-6 px-4">
        {/* Step 3 (Active) */}
        <div className="flex flex-col items-center">
          <div className="w-7 h-7 rounded-full bg-[#1F6BFF] text-white flex items-center justify-center text-xs font-bold shadow-[0_0_12px_#1F6BFF] mb-1">
            ۳
          </div>
          <span className="text-[10px] text-[#1F6BFF] font-bold">تعیین رمز</span>
        </div>
        <div className="flex-1 h-0.5 bg-emerald-500 mx-2" />

        {/* Step 2 (Completed) */}
        <div className="flex flex-col items-center">
          <div className="w-7 h-7 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs font-bold mb-1">
            <Check className="w-4 h-4" />
          </div>
          <span className="text-[10px] text-emerald-400 font-medium">اطلاعات گارانتی</span>
        </div>
        <div className="flex-1 h-0.5 bg-emerald-500 mx-2" />

        {/* Step 1 (Completed) */}
        <div className="flex flex-col items-center">
          <div className="w-7 h-7 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs font-bold mb-1">
            <Check className="w-4 h-4" />
          </div>
          <span className="text-[10px] text-emerald-400 font-medium">ثبت دستگاه</span>
        </div>
      </div>

      {/* Fields */}
      <div className="flex-1 space-y-4 overflow-y-auto pb-4">
        {/* Password */}
        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1.5">
            رمز عبور دستگاه (۴ تا ۸ رقم)
          </label>
          <div className="relative">
            <input
              type={showPass ? 'text' : 'password'}
              dir="ltr"
              value={formData.password || ''}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              placeholder="••••••"
              className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3.5 py-3 text-sm text-white font-mono placeholder:text-gray-600 outline-none transition-colors pr-10"
            />
            <button
              type="button"
              onClick={() => setShowPass(!showPass)}
              className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white"
            >
              {showPass ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
            </button>
            <Lock className="w-4 h-4 text-gray-500 absolute right-3 top-1/2 -translate-y-1/2" />
          </div>

          {/* Password Strength Meter */}
          <div className="mt-2 flex items-center justify-between text-xs">
            <span className={`text-[11px] font-semibold ${
              strength.score === 1 ? 'text-red-400' : strength.score === 2 ? 'text-blue-400' : strength.score >= 3 ? 'text-emerald-400' : 'text-gray-500'
            }`}>
              {strength.text}
            </span>
            <div className="flex gap-1.5">
              {[1, 2, 3, 4].map((step) => (
                <div
                  key={step}
                  className={`w-6 h-1.5 rounded-full transition-all ${
                    strength.score >= step ? strength.color : 'bg-gray-700'
                  }`}
                />
              ))}
            </div>
          </div>
        </div>

        {/* Retype Password */}
        <div>
          <label className="block text-xs font-semibold text-gray-300 mb-1.5">
            تکرار رمز عبور
          </label>
          <div className="relative">
            <input
              type={showConfirmPass ? 'text' : 'password'}
              dir="ltr"
              value={formData.confirmPassword || ''}
              onChange={(e) => setFormData({ ...formData, confirmPassword: e.target.value })}
              placeholder="••••••"
              className="w-full bg-[#161B22] border border-[#2D333B] focus:border-[#1F6BFF] rounded-xl px-3.5 py-3 text-sm text-white font-mono placeholder:text-gray-600 outline-none transition-colors pr-10"
            />
            <button
              type="button"
              onClick={() => setShowConfirmPass(!showConfirmPass)}
              className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white"
            >
              {showConfirmPass ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
            </button>
            <Lock className="w-4 h-4 text-gray-500 absolute right-3 top-1/2 -translate-y-1/2" />
          </div>
        </div>

        {/* Biometric Toggle Card */}
        <div className="p-4 rounded-2xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between">
          <div className="flex items-center gap-3">
            <button
              type="button"
              onClick={() => {
                playSound('click');
                setFormData({ ...formData, biometric: !formData.biometric });
              }}
              className={`w-12 h-6 rounded-full transition-colors relative p-0.5 ${
                formData.biometric ? 'bg-[#1F6BFF]' : 'bg-[#2D333B]'
              }`}
            >
              <div className={`w-5 h-5 rounded-full bg-white transition-transform ${
                formData.biometric ? '-translate-x-6' : 'translate-x-0'
              }`} />
            </button>
          </div>

          <div className="text-right">
            <h4 className="text-xs font-bold text-white mb-0.5">فعال‌سازی اثر انگشت / چهره</h4>
            <p className="text-[11px] text-gray-400">ورود سریع‌تر بدون نیاز به تایپ مکرر رمز</p>
          </div>

          <div className="w-10 h-10 rounded-xl bg-[#1F6BFF]/10 text-[#1F6BFF] flex items-center justify-center">
            <Fingerprint className="w-5 h-5" />
          </div>
        </div>

        {/* Info Banner */}
        <div className="p-3 rounded-xl bg-[#161B22]/60 border border-[#2D333B] flex items-center gap-2.5 text-gray-400 text-xs">
          <Info className="w-4 h-4 text-[#1F6BFF] shrink-0" />
          <p className="text-[11px] leading-relaxed">
            رمز عبور شما به صورت امن و هش‌شده در حافظه دزدگیر و ماژول ذخیره می‌شود.
          </p>
        </div>
      </div>

      {/* Complete Button */}
      <div className="pt-3">
        <button
          onClick={() => {
            playSound('arm');
            onComplete();
          }}
          className="w-full py-3.5 px-6 rounded-2xl bg-[#1F6BFF] hover:bg-[#1A5BDB] text-white font-bold text-sm shadow-[0_0_25px_rgba(31,107,255,0.5)] transition-all flex items-center justify-center gap-2"
        >
          <ShieldCheck className="w-4 h-4" />
          <span>تکمیل ثبت‌نام و ورود به سامانه KDD</span>
        </button>
      </div>
    </div>
  );
}
''')

    print("Screens 01-05 created!")

create_screens()
