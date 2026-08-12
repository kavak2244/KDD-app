import React, { useState } from 'react';
import { Shield, Bell, CheckCircle2, RotateCw } from 'lucide-react';
import { ASSET_TRUCK_ORIG_CLEAN, ASSET_SHIELD_PURE_CIRCLE } from '../assetsBase64';
import { playSound } from '../utils/audio';

export default function Screen06_Dashboard({
  device,
  isArmed,
  onToggleArm,
  onOpenNotifications,
  onRefreshStatus,
  unreadCount = 0,
}) {
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [refreshToast, setRefreshToast] = useState(false);

  const handleRefreshClick = () => {
    if (isRefreshing) return;
    playSound('click');
    setIsRefreshing(true);
    setRefreshToast(true);

    if (onRefreshStatus) {
      onRefreshStatus();
    }

    setTimeout(() => {
      setIsRefreshing(false);
      playSound('arm');
      setTimeout(() => {
        setRefreshToast(false);
      }, 2000);
    }, 1000);
  };

  return (
    <div className="w-full flex flex-col p-3.5 sm:p-4 bg-[#0D1117] text-right select-none space-y-3.5" dir="rtl">
      {/* Toast Notification on Refresh */}
      {refreshToast && (
        <div className="fixed top-12 left-1/2 -translate-x-1/2 z-50 px-4 py-2 rounded-full bg-[#1F6BFF] text-white text-xs font-bold shadow-[0_0_20px_rgba(31,107,255,0.8)] flex items-center gap-2 animate-fadeIn">
          {isRefreshing ? (
            <>
              <RotateCw className="w-4 h-4 animate-spin" />
              <span>در حال استعلام وضعیت از SIM800...</span>
            </>
          ) : (
            <>
              <CheckCircle2 className="w-4 h-4" />
              <span>وضعیت دستگاه با موفقیت به‌روزرسانی شد</span>
            </>
          )}
        </div>
      )}

      {/* Top Header: Brand on Right (RTL), Action Icons on Left */}
      <div className="flex items-center justify-between pt-1 px-1">
        {/* Right: KDD Brand */}
        <span className="text-lg font-black text-white tracking-widest font-sans">KDD</span>

        {/* Left: Refresh Button + Notification Bell */}
        <div className="flex items-center gap-2">
          {/* Refresh Button */}
          <button
            onClick={handleRefreshClick}
            disabled={isRefreshing}
            title="به‌روزرسانی وضعیت دستگاه"
            className="p-2 rounded-xl text-gray-300 hover:text-[#1F6BFF] bg-[#161B22]/60 hover:bg-[#161B22] border border-[#2D333B] transition-all"
          >
            <RotateCw className={`w-4 h-4 stroke-[2.2] ${isRefreshing ? 'animate-spin text-[#1F6BFF]' : ''}`} />
          </button>

          {/* Notification Bell */}
          <button
            onClick={() => {
              playSound('click');
              onOpenNotifications();
            }}
            className="relative p-2 rounded-xl text-gray-300 hover:text-white bg-[#161B22]/60 hover:bg-[#161B22] border border-[#2D333B] transition-colors"
          >
            <Bell className="w-4 h-4 stroke-[2]" />
            {unreadCount > 0 && (
              <span className="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full shadow-[0_0_6px_#EF4444]" />
            )}
          </button>
        </div>
      </div>

      {/* Card 1: Top Hero Container (RTL: FH500 on Right, Truck on Left) */}
      <div className="rounded-3xl bg-[#161B22] border border-[#242C37] p-4 relative overflow-hidden shadow-xl">
        {/* Top Row: Info on Right, Truck on Left */}
        <div className="flex items-center justify-between mb-3.5">
          {/* Right: Device Title & Status Chip */}
          <div className="text-right flex flex-col items-start pr-1">
            <h1 className="text-3xl font-black text-white mb-2 tracking-tight font-sans">
              {device?.name?.split('—')[0]?.trim() || 'FH500'}
            </h1>
            
            {/* Status Chip: سیستم متصل است */}
            <div className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-emerald-950/60 border border-emerald-500/40 text-emerald-400 text-xs font-semibold shadow-[0_0_12px_rgba(34,197,94,0.2)]">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 stroke-[2.4]" />
              <span>سیستم متصل است</span>
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            </div>
          </div>

          {/* Left: Original 3D Volvo FH500 Truck with Blue Energy Ring */}
          <div className="relative w-36 h-30 sm:w-40 sm:h-34 flex items-center justify-center shrink-0">
            <img
              src={ASSET_TRUCK_ORIG_CLEAN}
              alt="Volvo FH500 Truck"
              className="w-full h-full object-contain mix-blend-lighten transition-transform duration-300 hover:scale-105"
            />
          </div>
        </div>

        {/* Bottom Row: 2 Balanced Metric Cards side by side */}
        <div className="grid grid-cols-2 gap-3 pt-3 border-t border-[#2D333B]/70">
          {/* Right Box (RTL 1st): باتری دستگاه */}
          <div className="p-2.5 rounded-2xl bg-[#0D1117] border border-[#2D333B] flex items-center justify-between">
            <div className="text-right">
              <span className="text-[11px] text-gray-400 block mb-0.5 font-medium">باتری دستگاه</span>
              <span className="text-lg font-black text-white font-mono">{device?.battery || 98}٪</span>
            </div>

            {/* Battery Icon */}
            <div className="w-5 h-8 rounded-[4px] border-2 border-emerald-400 p-0.5 flex flex-col justify-end relative shadow-[0_0_8px_rgba(34,197,94,0.3)]">
              <div className="absolute -top-1 left-1/2 -translate-x-1/2 w-2 h-0.5 bg-emerald-400 rounded-t-sm" />
              <div className="w-full h-4/5 bg-emerald-400 rounded-sm shadow-[0_0_6px_#22C55E]" />
            </div>
          </div>

          {/* Left Box (RTL 2nd): سیگنال GSM */}
          <div className="p-2.5 rounded-2xl bg-[#0D1117] border border-[#2D333B] flex items-center justify-between">
            <div className="text-right">
              <span className="text-[11px] text-gray-400 block mb-0.5 font-medium">سیگنال GSM</span>
              <span className="text-base font-black text-white">عالی</span>
            </div>

            {/* GSM Signal Bars */}
            <div className="flex items-end gap-1 h-5">
              <div className="w-1.5 h-1.5 bg-[#1F6BFF] rounded-sm" />
              <div className="w-1.5 h-2.5 bg-[#1F6BFF] rounded-sm" />
              <div className="w-1.5 h-4 bg-[#1F6BFF] rounded-sm" />
              <div className="w-1.5 h-5 bg-[#1F6BFF] rounded-sm shadow-[0_0_8px_#1F6BFF]" />
            </div>
          </div>
        </div>
      </div>

      {/* Card 2: Protection Status Card (RTL: Text & Switch on Right, Shield on Left) */}
      <div className="rounded-3xl bg-[#161B22] border border-[#242C37] p-4 sm:p-5 relative overflow-hidden shadow-xl flex items-center justify-between">
        {/* Right: Security Status, Title and Pill Switch */}
        <div className="text-right flex flex-col items-start justify-between py-1">
          <div>
            {/* Header Title with Outline Shield */}
            <div className="flex items-center gap-1.5 text-gray-200 mb-1.5">
              <Shield className="w-4 h-4 text-gray-400 stroke-[2]" />
              <span className="text-sm font-bold">سیستم حفاظتی</span>
            </div>

            {/* Status Text (فعال / غیرفعال) */}
            <h2 className={`text-4xl font-black mb-1 transition-colors ${
              isArmed ? 'text-emerald-400 drop-shadow-[0_0_15px_rgba(34,197,94,0.4)]' : 'text-blue-400'
            }`}>
              {isArmed ? 'فعال' : 'غیرفعال'}
            </h2>

            <p className="text-xs text-gray-400 mb-4">
              {isArmed ? 'حفاظت خودرو فعال است' : 'حفاظت خودرو غیرفعال است'}
            </p>
          </div>

          {/* Luxury Blue Pill Toggle Switch */}
          <button
            type="button"
            onClick={onToggleArm}
            className={`w-18 h-9 rounded-full p-1 transition-colors duration-300 relative cursor-pointer ${
              isArmed ? 'bg-[#1F6BFF] shadow-[0_0_18px_rgba(31,107,255,0.7)]' : 'bg-[#2D333B]'
            }`}
          >
            <div
              className={`w-7 h-7 rounded-full bg-white transition-transform duration-300 shadow-md ${
                isArmed ? '-translate-x-9' : 'translate-x-0'
              }`}
            />
          </button>
        </div>

        {/* Left: Clean Circular Blue Energy Ring Shield */}
        <div className="relative w-30 h-30 sm:w-34 sm:h-34 flex items-center justify-center shrink-0">
          <img
            src={ASSET_SHIELD_PURE_CIRCLE}
            alt="Blue Energy Shield"
            className={`w-full h-full object-contain transition-all duration-300 ${
              isArmed
                ? 'scale-105 filter drop-shadow-[0_0_22px_#1F6BFF]'
                : 'opacity-45 grayscale-[50%]'
            }`}
            style={{
              mixBlendMode: 'screen',
            }}
          />
        </div>
      </div>
    </div>
  );
}
