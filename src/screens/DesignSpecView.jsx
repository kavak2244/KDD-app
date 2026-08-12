import React from 'react';
import {
  ASSET_SCREEN_01,
  ASSET_SCREEN_02,
  ASSET_SCREEN_03,
  ASSET_SCREEN_04,
  ASSET_SCREEN_05,
  ASSET_SCREEN_06,
  ASSET_SCREEN_07,
  ASSET_SCREEN_08,
  ASSET_SCREEN_09,
  ASSET_SCREEN_10,
  ASSET_SCREEN_11,
  ASSET_SCREEN_12,
  ASSET_SCREEN_13,
  ASSET_SCREEN_14,
} from '../assetsBase64';
import { Palette, Type, Terminal } from 'lucide-react';

export default function DesignSpecView({ onSelectScreen }) {
  const screensList = [
    { num: '01', title: 'Splash / شروع اپ', desc: 'نمایش هویت KDD و حلقه نوری Blue Energy Ring', img: ASSET_SCREEN_01, key: 'splash' },
    { num: '02', title: 'دستگاه‌های من', desc: 'انتخاب دستگاه یا افزودن خودرو جدید', img: ASSET_SCREEN_02, key: 'my-devices' },
    { num: '03', title: 'ثبت دستگاه — مرحله ۱', desc: 'شناسه، نام دستگاه و سیم‌کارت فعال', img: ASSET_SCREEN_03, key: 'register-1' },
    { num: '04', title: 'ثبت گارانتی — مرحله ۲', desc: 'اطلاعات مالک، موقعیت و تکنسین', img: ASSET_SCREEN_04, key: 'register-2' },
    { num: '05', title: 'تعیین رمز عبور — مرحله ۳', desc: 'رمز عبور و فعال‌سازی اثر انگشت', img: ASSET_SCREEN_05, key: 'register-3' },
    { num: '06', title: 'داشبورد / خانه', desc: 'مرکز فرمان اصلی، آلارم، باتری و آنتن', img: ASSET_SCREEN_06, key: 'dashboard' },
    { num: '07', title: 'تنظیمات', desc: 'دسترسی دسته‌بندی‌شده به کلیه زیرسیستم‌ها', img: ASSET_SCREEN_07, key: 'settings' },
    { num: '08', title: 'وضعیت دستگاه', desc: 'تله‌متری زنده ولتاژها، سنسورها و رله‌ها', img: ASSET_SCREEN_08, key: 'status' },
    { num: '09', title: 'خروجی‌ها', desc: 'کنترل و تغییر نام ۸ رله سخت‌افزاری', img: ASSET_SCREEN_09, key: 'outputs' },
    { num: '10', title: 'تنظیمات دستگاه', desc: 'سخت‌افزار، پیامک‌ها، زبان و آژیر', img: ASSET_SCREEN_10, key: 'device-settings' },
    { num: '11', title: 'کدگذاری ریموت', desc: 'شبیه‌ساز فیزیکی توالی کلیدهای ریموت', img: ASSET_SCREEN_11, key: 'remote-coding' },
    { num: '12', title: 'ریموت‌ها', desc: 'مدیریت ۱۰ ریموت، پارتیشن و قفل امنیتی', img: ASSET_SCREEN_12, key: 'remotes' },
    { num: '13', title: 'مخاطبین', desc: 'ماتریس دسترسی مخاطبین (تماس، SMS، ادمین)', img: ASSET_SCREEN_13, key: 'contacts' },
    { num: '14', title: 'سنسورها', desc: 'تنظیم ۸ سنسور (پارتیشن، NO/NC، ۲۴ ساعته)', img: ASSET_SCREEN_14, key: 'sensors' },
  ];

  return (
    <div className="w-full min-h-screen bg-[#080C12] text-gray-200 p-6">
      {/* Header */}
      <div className="max-w-6xl mx-auto mb-8 text-right">
        <div className="flex items-center justify-between mb-3 border-b border-[#2D333B] pb-4">
          <span className="text-xs px-3 py-1 rounded-full bg-[#1F6BFF]/20 text-[#1F6BFF] border border-[#1F6BFF]/40 font-mono">
            KDD Design System v1.1 — Reference Specs
          </span>
          <h1 className="text-2xl font-black text-white">سند طراحی و مشخصات فنی اپلیکیشن KDD</h1>
        </div>
        <p className="text-sm text-gray-400">
          برای تست و اجرای زنده هر صفحه، روی کارت آن کلیک کنید.
        </p>
      </div>

      {/* Design System Tokens Summary */}
      <div className="max-w-6xl mx-auto mb-10 grid grid-cols-1 md:grid-cols-3 gap-4 text-right">
        <div className="p-4 rounded-2xl bg-[#161B22] border border-[#2D333B]">
          <div className="flex items-center gap-2 mb-3 text-[#1F6BFF]">
            <Palette className="w-5 h-5" />
            <h3 className="text-sm font-bold text-white">پالت رنگی برند</h3>
          </div>
          <div className="grid grid-cols-2 gap-2 text-xs font-mono">
            <div className="flex items-center gap-2">
              <span className="w-4 h-4 rounded bg-[#1F6BFF] shadow-[0_0_8px_#1F6BFF]" />
              <span>Primary #1F6BFF</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-4 h-4 rounded bg-[#0D1117] border border-gray-700" />
              <span>Bg #0D1117</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-4 h-4 rounded bg-[#161B22] border border-gray-700" />
              <span>Card #161B22</span>
            </div>
            <div className="flex items-center gap-2">
              <span className="w-4 h-4 rounded bg-[#22C55E]" />
              <span>Success #22C55E</span>
            </div>
          </div>
        </div>

        <div className="p-4 rounded-2xl bg-[#161B22] border border-[#2D333B]">
          <div className="flex items-center gap-2 mb-3 text-[#1F6BFF]">
            <Type className="w-5 h-5" />
            <h3 className="text-sm font-bold text-white">تایپوگرافی و ساختار RTL</h3>
          </div>
          <ul className="text-xs space-y-1.5 text-gray-300">
            <li>• فونت فارسی: <strong className="text-white">Vazirmatn / IRANYekanX</strong></li>
            <li>• عناوین صفحات: Bold ۲۴px</li>
            <li>• دکمه‌های اصلی: Medium ۱۶px</li>
          </ul>
        </div>

        <div className="p-4 rounded-2xl bg-[#161B22] border border-[#2D333B]">
          <div className="flex items-center gap-2 mb-3 text-[#1F6BFF]">
            <Terminal className="w-5 h-5" />
            <h3 className="text-sm font-bold text-white">لایه ارتباطی ماژول SIM800</h3>
          </div>
          <ul className="text-xs space-y-1.5 text-gray-300">
            <li>• روش ۱: اینترنت ابری (MQTT / TCP Socket)</li>
            <li>• روش ۲: پیامک اضطراری (GSM SMS Fallback)</li>
          </ul>
        </div>
      </div>

      {/* 14 Screens Grid */}
      <div className="max-w-6xl mx-auto">
        <h2 className="text-lg font-bold text-white mb-4 text-right">طرح تمام ۱۴ صفحه اصلی (روی هر صفحه برای تست زنده کلیک کنید):</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-5">
          {screensList.map((sc) => (
            <div
              key={sc.num}
              onClick={() => onSelectScreen(sc.key)}
              className="bg-[#161B22] border border-[#2D333B] hover:border-[#1F6BFF] hover:shadow-[0_0_25px_rgba(31,107,255,0.3)] rounded-2xl overflow-hidden cursor-pointer transition-all flex flex-col group"
            >
              {/* Screen Preview Image */}
              <div className="relative aspect-[9/16] bg-black/60 overflow-hidden">
                <img
                  src={sc.img}
                  alt={sc.title}
                  className="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-300"
                />
                <div className="absolute top-3 right-3 px-2 py-0.5 rounded-md bg-black/70 backdrop-blur-md text-[11px] font-mono text-[#1F6BFF] font-bold border border-[#1F6BFF]/40">
                  #{sc.num}
                </div>
                <div className="absolute inset-0 bg-gradient-to-t from-[#161B22] via-transparent to-transparent opacity-80" />
                
                <div className="absolute bottom-3 left-3 right-3 flex items-center justify-between">
                  <span className="text-xs font-bold text-white group-hover:text-[#1F6BFF] transition-colors">
                    تست و تعامل زنده ➔
                  </span>
                </div>
              </div>

              {/* Title and Desc */}
              <div className="p-3 text-right flex-1 flex flex-col justify-between">
                <div>
                  <h3 className="text-sm font-bold text-white mb-1 group-hover:text-[#1F6BFF] transition-colors">{sc.title}</h3>
                  <p className="text-[11px] text-gray-400 leading-relaxed">{sc.desc}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
