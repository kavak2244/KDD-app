import React from 'react';
import { Shield, ShieldCheck, Battery, Zap, Signal, Wifi, Radio, Power, RefreshCw, CheckCircle2, AlertTriangle } from 'lucide-react';
import { playSound } from '../utils/audio';

export default function Screen08_DeviceStatus({ device, sensors, relays, onTriggerSensor, isArmed }) {
  return (
    <div className="min-h-full flex flex-col p-4 bg-[#0D1117] text-right">
      <div className="mb-4 pt-1">
        <h2 className="text-xl font-bold text-white mb-1">وضعیت کلی دستگاه</h2>
        <p className="text-xs text-gray-400">تله‌متری زنده سنسورها، ولتاژ باتری و شبکه ارتباطی</p>
      </div>

      <div className="flex-1 space-y-4 overflow-y-auto pb-4">
        {/* Status Header Card */}
        <div className="p-4 rounded-2xl bg-gradient-to-b from-[#161B22] to-[#12171F] border border-[#2D333B] flex items-center justify-between">
          <div className="w-12 h-12 rounded-2xl bg-[#1F6BFF]/15 border border-[#1F6BFF]/40 text-[#1F6BFF] flex items-center justify-center shadow-[0_0_20px_rgba(31,107,255,0.3)]">
            <ShieldCheck className="w-7 h-7" />
          </div>
          <div className="text-right">
            <div className="flex items-center justify-end gap-2 mb-0.5">
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
              <h3 className="text-base font-bold text-emerald-400">سیستم متصل و آنلاین است</h3>
            </div>
            <p className="text-xs text-gray-400">وضعیت اجزای سخت‌افزاری و برقراری ارتباط</p>
          </div>
        </div>

        {/* Telemetry Key/Value Rows */}
        <div className="rounded-2xl bg-[#161B22] border border-[#2D333B] divide-y divide-[#2D333B]/60 overflow-hidden">
          <div className="p-3 flex items-center justify-between text-xs">
            <span className="font-semibold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded">متصل (Ready)</span>
            <div className="flex items-center gap-2 text-gray-300">
              <span>وضعیت ماژول SIM800:</span>
              <Radio className="w-4 h-4 text-[#1F6BFF]" />
            </div>
          </div>

          <div className="p-3 flex items-center justify-between text-xs">
            <span className="font-mono font-semibold text-white">98% (12.8V DC)</span>
            <div className="flex items-center gap-2 text-gray-300">
              <span>باتری پشتیبان:</span>
              <Battery className="w-4 h-4 text-emerald-400" />
            </div>
          </div>

          <div className="p-3 flex items-center justify-between text-xs">
            <span className="font-mono font-semibold text-emerald-400">وصل (24.2V دینام)</span>
            <div className="flex items-center gap-2 text-gray-300">
              <span>برق ورودی خودرو:</span>
              <Zap className="w-4 h-4 text-amber-400" />
            </div>
          </div>

          <div className="p-3 flex items-center justify-between text-xs">
            <span className="font-semibold text-white">عالی (28/31 RSSI)</span>
            <div className="flex items-center gap-2 text-gray-300">
              <span>قدرت آنتن GSM:</span>
              <Signal className="w-4 h-4 text-blue-400" />
            </div>
          </div>

          <div className="p-3 flex items-center justify-between text-xs">
            <span className="font-semibold text-emerald-400">آنلاین (GPRS / 4G)</span>
            <div className="flex items-center gap-2 text-gray-300">
              <span>شبکه اینترنت:</span>
              <Wifi className="w-4 h-4 text-[#1F6BFF]" />
            </div>
          </div>
        </div>

        {/* Live Sensors Grid (8 Sensors) */}
        <div>
          <div className="flex items-center justify-between mb-2">
            <span className="text-[11px] text-gray-500 font-mono">لمس هر سنسور = تست شبیه‌سازی تحریک</span>
            <h4 className="text-xs font-bold text-gray-300">وضعیت سنسورها (۸ زون)</h4>
          </div>

          <div className="grid grid-cols-2 gap-2">
            {sensors.map((s) => (
              <button
                key={s.id}
                onClick={() => {
                  playSound('click');
                  onTriggerSensor(s.id);
                }}
                className={`p-2.5 rounded-xl border flex items-center justify-between transition-all ${
                  s.isTriggered
                    ? 'bg-red-500/20 border-red-500 text-red-300 shadow-[0_0_15px_rgba(239,68,68,0.4)]'
                    : 'bg-[#161B22] border-[#2D333B] text-gray-300 hover:border-gray-600'
                }`}
              >
                <span className={`text-[10px] px-1.5 py-0.5 rounded font-bold ${
                  s.isTriggered ? 'bg-red-500 text-white' : 'bg-emerald-500/20 text-emerald-400'
                }`}>
                  {s.isTriggered ? 'تحریک شد!' : 'فعال'}
                </span>

                <span className="text-xs font-medium truncate max-w-[100px]">
                  سنسور {s.id}
                </span>
              </button>
            ))}
          </div>
        </div>

        {/* Live Outputs Grid (8 Relays) */}
        <div>
          <div className="flex items-center justify-between mb-2">
            <span className="text-[11px] text-gray-500 font-mono">وضعیت قطع و وصل رله‌ها</span>
            <h4 className="text-xs font-bold text-gray-300">وضعیت خروجی‌ها (۸ رله)</h4>
          </div>

          <div className="grid grid-cols-2 gap-2">
            {relays.map((r) => (
              <div
                key={r.id}
                className="p-2.5 rounded-xl bg-[#161B22] border border-[#2D333B] flex items-center justify-between text-xs"
              >
                <span className={`text-[10px] px-1.5 py-0.5 rounded font-bold ${
                  r.state ? 'bg-[#1F6BFF]/20 text-[#1F6BFF]' : 'bg-gray-800 text-gray-400'
                }`}>
                  {r.state ? 'روشن' : 'خاموش'}
                </span>
                <span className="text-gray-300 truncate max-w-[100px]">
                  خروجی {r.id}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
