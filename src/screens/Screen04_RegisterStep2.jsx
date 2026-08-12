import React from 'react';
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
