
## trip 30pt,484solves
```
What road was this this photo taken on?

For example, if the road was "Colesville Road" the flag would be actf{colesville}.
```
写真が与えられてどこで撮られたのかを回答する問題。
[【CTF】OSINT問題で個人的に使用するツール・サイト・テクニックまとめ](https://qiita.com/xryuseix/items/e35b8c946e5dfe96f848)を参照し、google lensや画像検索など色々試しましたが、一致する画像が出てこなかった為、断念しました。

[こちらのwriteupを参考に](https://github.com/raghavtwenty/capture-the-flags/tree/main/angstrom_ctf_2024/trip)

画像ファイルを取得
```
wget https://files.actf.co/fdea3784a76afd8110498bd596653c433e3f5206bc0fa87f28a5edbd0a622ceb/trip.jpeg
```
exif情報を取得
```
exif trip.jpeg  
```
出力結果
```
EXIF tags in 'trip.jpeg' ('Motorola' byte order):
--------------------+----------------------------------------------------------
Tag                 |Value
--------------------+----------------------------------------------------------
Manufacturer        |Apple
Model               |iPhone 15 Pro
Orientation         |Top-left
X-Resolution        |72
Y-Resolution        |72
Resolution Unit     |Inch
Software            |17.4.1
Date and Time       |2024:04:18 05:54:34
Exposure Time       |1/33 sec.
F-Number            |f/1.8
Exposure Program    |Normal program
ISO Speed Ratings   |1000
Exif Version        |Exif Version 2.32
Date and Time (Origi|2024:04:18 05:54:34
Date and Time (Digit|2024:04:18 05:54:34
Offset Time For Date|-04:00
Offset Time For Date|-04:00
Offset Time For Date|-04:00
Shutter Speed       |5.03 EV (1/33 sec.)
Aperture            |1.66 EV (f/1.8)
Brightness          |-1.96 EV (0.88 cd/m^2)
Exposure Bias       |0.00 EV
Metering Mode       |Pattern
Flash               |Flash did not fire, compulsory flash mode
Focal Length        |6.8 mm
Subject Area        |Within rectangle (width 3291, height 1884) around (x,y) = 
Maker Note          |1723 bytes undefined data
Sub-second Time (Ori|337
Sub-second Time (Dig|337
Color Space         |Uncalibrated
Pixel X Dimension   |5712
Pixel Y Dimension   |4284
Sensing Method      |One-chip color area sensor
Scene Type          |Directly photographed
Exposure Mode       |Auto exposure
White Balance       |Auto white balance
Focal Length in 35mm|24
Lens Specification  |2.220000,  9, 1.780000, 2.8
Lens Make           |Apple
Lens Model          |iPhone 15 Pro back triple camera 6.765mm f/1.78
Composite Image     |2
FlashPixVersion     |FlashPix Version 1.0
North or South Latit|N
Latitude            |37, 56, 23.60
East or West Longitu|W
Longitude           |75, 26, 17.11
Altitude Reference  |Sea level
Altitude            |1.01584
GPS Time (Atomic Clo|09:54:33.79
Speed Unit          |K
Speed of GPS Receive|24.3030
GPS Image Direction |T
GPS Image Direction |101.5118
Reference for Bearin|T
Bearing of Destinati|101.5118
GPS Date            |2024:04:18
GPS Horizontal Posit|4.7887
--------------------+----------------------------------------------------------

```

こちらの緯度経度情報をgooglemapに打ち込みます。
```
North or South Latit|N
Latitude            |37, 56, 23.60
East or West Longitu|W
Longitude           |75, 26, 17.11
```
```
37°56'23.6"N 75°26'17.1"W
```
```
actf{Chincoteague}
```
