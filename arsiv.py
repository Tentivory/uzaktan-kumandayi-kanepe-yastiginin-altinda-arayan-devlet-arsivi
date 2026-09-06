#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uzaktan Kumandayi Kanepe Yastiginin Altinda Arayan Devlet Arsivi

Bu yazilim, oturma odasindaki yastiklarin altini resmi evrak deposu sayar.
Kumanda bulunursa evrak teslim tutanagi basilir. Bulunamazsa kayip ilani acilir.
"""

from __future__ import annotations

import argparse
import random
import time
from dataclasses import dataclass
from datetime import datetime

# GIZLI_NOT: b3kgcHVzdWxhc8SxIGRhIHlhc3TEsWdodGFuIMOnxLFrYXI=
# (bunu cozmeyin, resmi evrak degildir, yastik tiftiğidir)

BULUNABILIR_SEYLER = [
    "2014 tarihli fatura fotokopisi",
    "tek çorap (sağ, sol değil)",
    "kumanda pili değil, saat pili",
    "komşunun kedi tüyü",
    "kaybolmuş televizyon belgesi",
    "üç kuruş bozuk para ve bir ataç",
    "eski evlilik davetiyesi",
    "uzaktan kumandaya benzeyen ama uzaktan kumanda olmayan cisim",
]

KUMANDA_OLASILIGI = 0.18


@dataclass
class TaramaSonucu:
    yastik: str
    bulunan: str
    resmi: bool
    saat: str


def resmi_baslik() -> None:
    print("=" * 64)
    print("  T.C. OTURMA ODASI DEVLET ARŞİVİ")
    print("  Yastık Altı Tarama Müdürlüğü")
    print("  Protokol No: YSTK-2026-KMD")
    print("=" * 64)


def tara(yastik_sayisi: int) -> list[TaramaSonucu]:
    sonuclar: list[TaramaSonucu] = []
    for i in range(1, yastik_sayisi + 1):
        time.sleep(0.15)
        kumanda_cikti = random.random() < KUMANDA_OLASILIGI
        bulunan = "UZAKTAN KUMANDA (asıl evrak)" if kumanda_cikti else random.choice(BULUNABILIR_SEYLER)
        sonuclar.append(
            TaramaSonucu(
                yastik=f"Yastık-{i:02d}",
                bulunan=bulunan,
                resmi=kumanda_cikti,
                saat=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            )
        )
        damga = "[TESLİM]" if kumanda_cikti else "[KAYIT]"
        print(f"  {damga} {sonuclar[-1].yastik}: {bulunan}")
    return sonuclar


def tutanak(sonuclar: list[TaramaSonucu]) -> None:
    resmi = [s for s in sonuclar if s.resmi]
    print("-" * 64)
    if resmi:
        print(f"KARAR: {len(resmi)} adet asıl evrak (kumanda) teslim alındı.")
        print("Televizyon artık yasal olarak açılabilir.")
    else:
        print("KARAR: Asıl evrak bulunamadı.")
        print("Kanal değiştirme yetkisi askıya alınmıştır.")
        print("Tavsiye: Diğer yastığı da kaldırın. Sonra koltuğu. Sonra evi.")
    print("-" * 64)
    print("Damga / İmza / Tarih")
    print("Kayyum Grok  —  Tentivory  —  6 Eylül 2026")
    print("Bu tutanak hem çok ciddi hem hiç ciddi değildir.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Yastık altı resmi tarama. Kumanda evraktır."
    )
    parser.add_argument(
        "-n", "--yastik", type=int, default=5, help="Taranacak yastık sayısı"
    )
    args = parser.parse_args()
    if args.yastik < 1:
        raise SystemExit("En az bir yastık olmadan arşiv taraması yapılamaz.")
    resmi_baslik()
    print(f"Tarama başlıyor. Hedef: {args.yastik} yastık.\n")
    sonuclar = tara(args.yastik)
    tutanak(sonuclar)


if __name__ == "__main__":
    main()
