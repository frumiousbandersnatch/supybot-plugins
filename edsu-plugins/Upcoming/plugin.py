from supybot.commands import *
import supybot.callbacks as callbacks

import feedparser

class Upcoming (callbacks.Privmsg):

    places = { \
        "kabul" : 855,
        "tirana" : 362,
        "town" : 953,
        "buenos aires" : 946,
        "ciudad de buenos aires" : 945,
        "buenos aires" : 497,
        "ciudad de buenos aires" : 127,
        "gessel" : 947,
        "rosario" : 616,
        "atlantic ocean" : 205,
        "caribbean sea" : 207,
        "indian ocean" : 209,
        "mediterranean sea" : 208,
        "pacific ocean" : 206,
        "all states" : 994,
        "australian capital territory" : 298,
        "new south wales" : 106,
        "northern territory" : 576,
        "queensland" : 116,
        "south australia" : 331,
        "tasmania" : 393,
        "victoria" : 145,
        "western australia" : 102,
        "burgenland" : 940,
        "lenz" : 291,
        "linz" : 506,
        "lower austria" : 773,
        "salzburg" : 659,
        "steiermark" : 950,
        "tyrol" : 547,
        "upper austria" : 605,
        "vienna" : 89,
        "eastern kingdoms" : 992,
        "kalimdor" : 991,
        "bahrain" : 530,
        "blue oyster cult" : 838,
        "of a revolution - o.a.r." : 850,
        "dhaka" : 885,
        "biscay" : 446,
        "minskaya oblast" : 812,
        "aalst" : 879,
        "antwerpen" : 62,
        "beveren" : 843,
        "brabant wallon" : 923,
        "brussels" : 238,
        "leopoldsburg" : 842,
        "li&#232;ge" : 493,
        "lier" : 873,
        "limburg" : 246,
        "maaseik" : 841,
        "oost-vlaanderen" : 61,
        "vlaams brabant" : 594,
        "vlaanderen" : 370,
        "wallonie" : 494,
        "west-vlaanderen" : 60,
        "bermuda" : 414,
        "st. george&#39;s" : 413,
        "beni" : 781,
        "chuquisaca" : 780,
        "cochabamba" : 775,
        "la paz" : 776,
        "oruro" : 779,
        "pando" : 782,
        "potos&#237;" : 783,
        "santa cruz" : 777,
        "tarija" : 778,
        "cochabamba" : 887,
        "sarajevo" : 794,
        "bahia" : 180,
        "cear&#225;" : 181,
        "distrito federal" : 705,
        "espirito santo" : 511,
        "minas gerais" : 179,
        "paran&#225;" : 507,
        "pernambuco" : 702,
        "rio de janeiro" : 178,
        "rio grande do norte" : 398,
        "rio grande do sul" : 177,
        "santa catarina" : 174,
        "s&#227;o paulo" : 172,
        "plovdiv" : 415,
        "ruse" : 811,
        "sofia" : 133,
        "varna" : 545,
        "banteay meanchey" : 749,
        "battambang" : 746,
        "kampong cham" : 758,
        "kampong chhnang" : 748,
        "kampong speu" : 756,
        "kampong thom" : 750,
        "kampot" : 753,
        "kandal" : 759,
        "koh kong" : 757,
        "kom pong som" : 711,
        "krati&#233;" : 764,
        "mondul kiri" : 754,
        "oddor meanchey" : 760,
        "phnom penh" : 708,
        "preah vihear" : 761,
        "prey veng" : 709,
        "pursat" : 747,
        "rattanak kiri" : 755,
        "siem reap" : 710,
        "stung treng" : 765,
        "svay rieng" : 751,
        "takeo" : 752,
        "alberta" : 76,
        "british columbia" : 55,
        "manitoba" : 73,
        "new brunswick" : 284,
        "newfoundland" : 533,
        "nova scotia" : 97,
        "nunavut" : 897,
        "ontario" : 54,
        "prince edward island" : 229,
        "quebec" : 53,
        "saskatchewan" : 79,
        "yukon" : 534,
        "antofagasta" : 513,
        "araucania" : 890,
        "concepcion" : 858,
        "puerto varas" : 822,
        "regi&#243;n de los rios" : 857,
        "santiago" : 394,
        "temuco" : 889,
        "anhui" : 877,
        "beijing" : 171,
        "changsha" : 693,
        "chengdu" : 487,
        "chongqing" : 797,
        "fujian" : 739,
        "gansu" : 645,
        "guangdong" : 442,
        "guangzhou" : 441,
        "heilongjiang" : 606,
        "henan" : 712,
        "hubei" : 447,
        "hunan" : 694,
        "hunan" : 961,
        "jiangsu" : 621,
        "jiangxi" : 706,
        "jinan" : 573,
        "liaoning" : 510,
        "nanjing" : 723,
        "shaanxi" : 989,
        "shanghai" : 170,
        "shenyang" : 807,
        "shenzhen" : 384,
        "taiyuan" : 762,
        "tianjin" : 310,
        "wuhan" : 502,
        "xiamen" : 501,
        "xinjiang" : 968,
        "yunnan" : 678,
        "yunnang" : 632,
        "zhejiang" : 505,
        "antioquia" : 448,
        "atlantico" : 217,
        "cundinamarca" : 443,
        "antioquia" : 697,
        "guanacaste" : 931,
        "nosara" : 930,
        "san jose" : 376,
        "croatia" : 696,
        "istra" : 538,
        "split" : 390,
        "zagreb" : 372,
        "cyprus" : 557,
        "larnaca" : 658,
        "limassol" : 655,
        "nicosia" : 656,
        "paphos" : 657,
        "&#268;echy" : 787,
        "czech republic" : 512,
        "ji&#382;n&#237; morava" : 688,
        "jihocesky kraj" : 292,
        "plzensky kraj" : 383,
        "severni morava" : 293,
        "aalborg" : 836,
        "copenhagen" : 125,
        "denmark" : 329,
        "nordsj&#230;lland" : 286,
        "&#197;rhus" : 169,
        "niedersachsen" : 960,
        "roseau" : 899,
        "st. george" : 900,
        "fifth world" : 366,
        "guayas" : 726,
        "alexandria" : 562,
        "cairo" : 375,
        "hurgada" : 840,
        "sharm el sheik, egypt" : 839,
        "engineering" : 924,
        "cadiz" : 767,
        "ciudad real" : 880,
        "lugo (galiza)" : 1021,
        "madrid" : 728,
        "mallorca (illes balears)" : 825,
        "santa cruz de tenerife" : 878,
        "tallinn" : 738,
        "harjumaa" : 863,
        "tallinn" : 333,
        "addis ababa" : 484,
        "chuuk" : 802,
        "yap" : 803,
        "ttf-bucksfan" : 365,
        "etel&#228;-suomen l&#228;&#228;ni" : 615,
        "helsinki area" : 184,
        "lappi" : 607,
        "l&#228;nsi suomi" : 283,
        "oulun l&#228;&#228;ni" : 400,
        "salo" : 680,
        "photo funtown" : 835,
        "alpes maritime" : 245,
        "alpes maritimes" : 260,
        "alsace" : 342,
        "aquitaine" : 343,
        "auvergne" : 1026,
        "auvergne" : 340,
        "basse-normandie" : 357,
        "bourgogne" : 345,
        "bretagne" : 344,
        "centre" : 346,
        "champagne-ardennes" : 347,
        "corse" : 348,
        "deauville" : 925,
        "d&#233;partement d&#39;outre-mer" : 360,
        "euro r&#233;gion" : 301,
        "franche-comt&#233;" : 349,
        "haute-normandie" : 356,
        "&#206;le-de-france" : 339,
        "languedoc-roussillon" : 350,
        "limousin" : 351,
        "loire" : 354,
        "lorraine" : 352,
        "lyon" : 305,
        "magny cours" : 819,
        "marseille" : 308,
        "midi-pyr&#233;n&#233;es" : 358,
        "monte carlo" : 926,
        "nantes" : 976,
        "nord" : 278,
        "normandie" : 353,
        "paris" : 126,
        "pas de calais" : 731,
        "pays de la loire" : 504,
        "picardie" : 359,
        "poitou-charentes" : 355,
        "provence alpes cotes d&#39;azur" : 309,
        "rh&#244;ne-alpes" : 341,
        "territoire d&#39;outre-mer" : 361,
        "vaucluse" : 281,
        "baden-w&#252;rttemberg" : 648,
        "baden-w&#252;rttenberg" : 88,
        "bamberg" : 686,
        "bavaria" : 57,
        "bayern" : 973,
        "berlin" : 74,
        "bremen" : 306,
        "darmstadt" : 941,
        "d&#252;sseldorf" : 1022,
        "flensburg" : 1020,
        "hamburg" : 113,
        "hessen" : 70,
        "karlsruhe" : 642,
        "karlsruhe/ettlingen" : 948,
        "lahr" : 690,
        "living room" : 682,
        "l&#252;beck" : 1019,
        "maintal" : 872,
        "mecklenburg-vorpommern" : 399,
        "munster" : 868,
        "m&#252;nchen" : 167,
        "niedersachsen" : 188,
        "nordrhein-westfalen" : 190,
        "nrw" : 860,
        "nurburgring" : 817,
        "region bodensee-oberschwaben" : 698,
        "rheinland-pfalz" : 69,
        "saarland" : 704,
        "sachsen-anhalt" : 392,
        "saxony" : 128,
        "schleswig-holstein" : 529,
        "th&#252;ringen" : 588,
        "th&#252;ringen" : 1025,
        "weimar" : 1024,
        "wuerzburg" : 962,
        "&#935;&#945;&#957;&#953;&#940;" : 984,
        "athens" : 579,
        "crete" : 983,
        "serre" : 829,
        "thessaloniki" : 828,
        "chiquimula" : 525,
        "guatemala" : 524,
        "region 4" : 288,
        "athens" : 542,
        "macedonia" : 531,
        "arctic" : 303,
        "island side" : 122,
        "kowloon" : 123,
        "lantau island" : 734,
        "new territories" : 124,
        "simply hong kong" : 912,
        "unknown" : 834,
        "budapest" : 78,
        "hajd&#250;-bihar megye" : 845,
        "andhrapradesh" : 929,
        "delhi" : 786,
        "india" : 1029,
        "karnataka" : 566,
        "kerala" : 905,
        "maharashtra" : 561,
        "tamilnadu" : 592,
        "uttar pradesh" : 707,
        "n/a" : 75,
        "andhra pradesh" : 261,
        "delhi" : 330,
        "goa" : 970,
        "gujarat" : 652,
        "gujarat" : 936,
        "haryana" : 823,
        "karnataka" : 266,
        "kerala" : 227,
        "madhya pradesh" : 323,
        "maharashtra" : 100,
        "meghalaya" : 555,
        "mizoram" : 556,
        "orissa" : 650,
        "pondicherry" : 1030,
        "punjab" : 296,
        "rajasthan" : 324,
        "tamil nadu" : 275,
        "tripura" : 624,
        "uttar pradesh" : 646,
        "west bengal" : 552,
        "andhra pradesh" : 933,
        "gujarat" : 906,
        "hyderabad" : 859,
        "tamilnadu" : 939,
        "uttar pradesh" : 982,
        "bali" : 687,
        "bandung" : 396,
        "batam" : 820,
        "bekasi" : 214,
        "east java" : 445,
        "gpib" : 662,
        "jakarta" : 201,
        "jawa timur" : 916,
        "nanggroe aceh darussalam" : 975,
        "surabaya" : 444,
        "west java" : 634,
        "international" : 716,
        "esfahan" : 891,
        "tehran" : 404,
        "cork" : 385,
        "county cork" : 495,
        "county dublin" : 71,
        "donegal" : 397,
        "galway" : 509,
        "kerry" : 745,
        "leitrim" : 800,
        "limerick" : 496,
        "louth" : 796,
        "target shooting" : 677,
        "tipperary" : 600,
        "waterford" : 391,
        "wexford" : 679,
        "co meath" : 806,
        "co. mayo" : 736,
        "dublin city" : 954,
        "bet-shemesh" : 450,
        "haifa" : 411,
        "israel" : 481,
        "jerusalem" : 332,
        "netanya" : 937,
        "tel-aviv" : 325,
        "ancona" : 135,
        "ascoli piceno" : 558,
        "avellino" : 595,
        "bari" : 608,
        "basilicata" : 980,
        "benevento" : 596,
        "bergamo" : 904,
        "bologna" : 382,
        "bolzano" : 886,
        "brescia" : 551,
        "cagliari" : 483,
        "cattolica" : 673,
        "como" : 417,
        "emilia-romagna" : 737,
        "firenze" : 553,
        "friuli venezia giulia" : 578,
        "genova" : 93,
        "italy" : 903,
        "lombardia" : 770,
        "lucca" : 276,
        "mantova" : 282,
        "matera" : 979,
        "milano" : 140,
        "monaco" : 818,
        "napoli" : 635,
        "padova" : 563,
        "palermo" : 763,
        "pisa" : 574,
        "pordenone" : 577,
        "roma" : 268,
        "san marino" : 816,
        "siena" : 874,
        "torino" : 437,
        "trento" : 262,
        "treviso" : 279,
        "veneto" : 280,
        "vicenza" : 676,
        "aichi" : 165,
        "akita" : 406,
        "all japan" : 290,
        "aomori" : 412,
        "chiba" : 320,
        "hiroshima" : 666,
        "hiroshima" : 418,
        "hokkaido" : 896,
        "hyogo" : 720,
        "iwate" : 407,
        "kanagawa" : 99,
        "kyoto" : 198,
        "mie" : 932,
        "nagasaki" : 644,
        "nagoya" : 971,
        "niigata" : 713,
        "okinawa" : 289,
        "osaka" : 691,
        "saga" : 769,
        "shiga" : 488,
        "tokyo" : 212,
        "yokohama" : 287,
        "amman" : 669,
        "aqaba" : 670,
        "irbid" : 671,
        "zarqa" : 672,
        "gwang-ju" : 986,
        "gyeonggi-do" : 985,
        "jeollabuk-do" : 987,
        "jeollanam-do" : 967,
        "seoul" : 131,
        "seoul" : 895,
        "kuwait" : 395,
        "rigas" : 335,
        "beirut" : 527,
        "beirut, lebanon" : 526,
        "vilnius" : 482,
        "luxembourg" : 491,
        "baja california" : 263,
        "chiapas" : 589,
        "coahuila" : 559,
        "colima" : 603,
        "distrito federal" : 228,
        "guanajuato" : 661,
        "jalisco" : 272,
        "michoac&#225;n" : 654,
        "morelos" : 766,
        "nayarit" : 541,
        "nuevo leon" : 277,
        "puebla" : 660,
        "quintana roo" : 653,
        "sonora" : 727,
        "tamaulipas" : 814,
        "veracruz" : 725,
        "macedonia" : 963,
        "toliara" : 788,
        "blantyre" : 909,
        "kedah" : 852,
        "kuala lumpur" : 597,
        "melaka" : 549,
        "pahang" : 898,
        "penang" : 864,
        "perak" : 821,
        "sabah" : 919,
        "sarawak" : 824,
        "selangor" : 674,
        "ciudad de m&#233;xico" : 637,
        "morelos" : 974,
        "nuevo leon" : 405,
        "north island" : 95,
        "south island" : 96,
        "managua" : 851,
        "rivas" : 1028,
        "lagos" : 952,
        "belfast" : 560,
        "akershus" : 204,
        "austagder" : 271,
        "buskerud" : 230,
        "hedmark" : 304,
        "hordaland" : 202,
        "nordtr&#248;ndelag" : 338,
        "oppland" : 255,
        "oslo" : 222,
        "oslo" : 223,
        "rogaland" : 248,
        "sogn of fjordane" : 363,
        "svalbard" : 243,
        "s&#248;rtr&#248;ndelag" : 254,
        "telemark" : 270,
        "telemark" : 192,
        "troms" : 485,
        "vestagder" : 242,
        "vestfold" : 269,
        "&#216;stfold" : 651,
        "anywhere" : 575,
        "cajamarca" : 955,
        "cusco" : 1027,
        "lima" : 408,
        "trujillo" : 957,
        "croatia" : 285,
        "hyderabad" : 801,
        "islamabad" : 668,
        "karachi" : 741,
        "lahore" : 789,
        "north west frontier province" : 808,
        "punjab" : 743,
        "sindh" : 742,
        "koror" : 618,
        "aklan" : 685,
        "butuan" : 714,
        "cebu" : 617,
        "la union" : 995,
        "manila" : 790,
        "marinduque" : 638,
        "metro manila" : 791,
        "ncr" : 103,
        "negros occidental" : 210,
        "surigao del norte" : 715,
        "bydgoszcz" : 893,
        "dolny slask" : 249,
        "malopolska" : 523,
        "podkarpackie" : 684,
        "poznan" : 486,
        "przemyieska" : 920,
        "szczecin" : 1018,
        "tr&#243;jmiasto" : 740,
        "warsaw" : 256,
        "a&#231;ores" : 593,
        "alentejo" : 318,
        "algarve" : 197,
        "aveiro" : 988,
        "beira interior" : 317,
        "beira litoral" : 314,
        "coimbra" : 311,
        "douro litoral" : 914,
        "entre douro e minho" : 315,
        "estremadura" : 196,
        "italy" : 724,
        "leiria" : 312,
        "lisbon" : 258,
        "minho" : 901,
        "porto" : 313,
        "tr&#225;s-os-montes e alto douro" : 316,
        "san juan" : 378,
        "doha" : 815,
        "bucharest" : 374,
        "cluj" : 647,
        "constanta" : 543,
        "iasi" : 626,
        "mures" : 598,
        "prahova" : 544,
        "satu mare" : 938,
        "far east" : 334,
        "kaliningrad" : 585,
        "kostroma region" : 981,
        "krasnodar krai" : 921,
        "krasnoyarskiy kray" : 935,
        "moscow" : 328,
        "novosibirsk" : 854,
        "omsk" : 381,
        "rostov-on-don" : 683,
        "st.petersburg" : 379,
        "sverdlovsk" : 732,
        "syberia" : 550,
        "syktyvkar" : 882,
        "vladimir" : 862,
        "volgograd" : 692,
        "voronezhskaya oblast" : 969,
        "jackson" : 870,
        "san diego" : 869,
        "san francisco" : 784,
        "san francisco" : 805,
        "silicon valley" : 804,
        "central province" : 609,
        "eastern province" : 610,
        "western province" : 611,
        "aberdeen" : 809,
        "edinburgh" : 643,
        "glasgow" : 810,
        "north lanarkshire" : 641,
        "south lanarkshire" : 640,
        "aq" : 922,
        "montenegro" : 844,
        "serbia" : 213,
        "bukit batok" : 861,
        "jurong west" : 219,
        "nanyang technological university" : 639,
        "np" : 449,
        "nus" : 978,
        "serangoon" : 622,
        "singapore" : 267,
        "toa payoh" : 554,
        "toh guan road" : 866,
        "west" : 965,
        "woodlands" : 636,
        "new hampshire" : 813,
        "bratislavsky kraj" : 364,
        "drava" : 591,
        "pitj" : 590,
        "earth" : 367,
        "fifth world" : 368,
        "gauteng" : 164,
        "western cape" : 118,
        "albacete" : 833,
        "alicante" : 499,
        "asturias" : 675,
        "avila" : 307,
        "barcelona" : 602,
        "bizkaia" : 389,
        "burgos" : 908,
        "cadiz" : 548,
        "catalunya" : 703,
        "cataluyna" : 108,
        "ciudad real" : 871,
        "cordoba" : 583,
        "galicia" : 326,
        "gipuzkoa" : 388,
        "granada" : 907,
        "huesca" : 297,
        "illes balears" : 911,
        "la coru&#241;a" : 722,
        "la rioja" : 735,
        "las palmas" : 774,
        "madrid" : 173,
        "madrid" : 771,
        "m&#225;laga" : 700,
        "murcia" : 500,
        "pontevedra" : 730,
        "salamanca" : 799,
        "santa cruz de tenerife" : 772,
        "segovia" : 917,
        "sevilla" : 582,
        "tarragona" : 883,
        "valencia" : 580,
        "valladolid" : 514,
        "vigo" : 795,
        "vizcaya" : 601,
        "zaragoza" : 729,
        "colombo" : 537,
        "castries" : 567,
        "dauphin" : 569,
        "dennery" : 572,
        "gros islet" : 568,
        "micoud" : 571,
        "praslin" : 570,
        "paramaribo" : 830,
        "blekinge" : 380,
        "dalarnas l&#228;n" : 517,
        "gotland" : 369,
        "g&#228;strikland" : 189,
        "g&#228;vleborgs l&#228;n" : 518,
        "g&#246;teborg" : 218,
        "hallands l&#228;n" : 519,
        "j&#228;mtlands l&#228;n" : 520,
        "kalmar l&#228;n" : 516,
        "kronobergsl&#228;n" : 521,
        "malm&#246;" : 264,
        "norrbotten" : 564,
        "sk&#229;ne" : 250,
        "stockholm" : 90,
        "uppsala" : 265,
        "v&#228;rmland" : 565,
        "v&#228;rmlands l&#228;n" : 515,
        "v&#228;sterbottens l&#228;n" : 522,
        "v&#228;sternorrland" : 604,
        "v&#228;stmanland" : 402,
        "&#214;rebro l&#228;n" : 966,
        "&#214;sterg&#246;tland" : 251,
        "aargau" : 421,
        "appenzell ausserrhoden" : 244,
        "appenzell innerrhoden" : 422,
        "basel" : 322,
        "basel-landschaft" : 436,
        "bern" : 114,
        "fribourg" : 294,
        "gen&#232;ve" : 319,
        "glarus" : 423,
        "grischun" : 424,
        "jura" : 425,
        "luzern" : 168,
        "neuch&#226;tel" : 420,
        "nidwalden" : 426,
        "obwalden" : 427,
        "schaffhausen" : 428,
        "schwyz" : 429,
        "solothurn" : 435,
        "st. gallen" : 434,
        "thurgau" : 433,
        "ticino" : 419,
        "uri" : 430,
        "valais" : 431,
        "vaud" : 274,
        "yverdone" : 910,
        "zug" : 432,
        "zurich" : 203,
        "aleppo" : 528,
        "damascus" : 503,
        "texas" : 958,
        "hsinchu" : 701,
        "hsintien" : 744,
        "nankang" : 934,
        "taipei" : 199,
        "bangkok" : 195,
        "chiangmai" : 1023,
        "hua hin" : 599,
        "eysturoy" : 231,
        "nor&#240;oyar" : 232,
        "nor&#240;urstreyoy" : 235,
        "sandoy" : 233,
        "su&#240;uroy" : 236,
        "su&#240;urstreymoy" : 237,
        "v&#225;gar" : 234,
        "amsterdam" : 633,
        "den haag" : 993,
        "eindhoven" : 972,
        "flevoland" : 247,
        "friesland" : 440,
        "gelderland" : 200,
        "groningen" : 81,
        "heerlen" : 719,
        "limburg" : 302,
        "noord brabant" : 295,
        "noord-holland" : 175,
        "overijssel" : 377,
        "utrecht" : 224,
        "zuid-holland" : 72,
        "houston" : 959,
        "arima" : 629,
        "chaguanas" : 630,
        "port-of-spain" : 627,
        "san fernando" : 628,
        "tunapuna" : 631,
        "nabeul" : 613,
        "tunis" : 489,
        "ege" : 540,
        "ic anadolu" : 539,
        "izmir" : 876,
        "karadeniz" : 689,
        "marmara" : 373,
        "uganda" : 681,
        "dnepr" : 336,
        "kriviy rih" : 337,
        "kyiv" : 220,
        "lviv" : 584,
        "mykolayiv" : 913,
        "abu dhabi" : 619,
        "dubai" : 620,
        "dubai" : 856,
        "bath" : 798,
        "bedfordshire" : 793,
        "berkshire" : 300,
        "berkshire" : 944,
        "boston, ma" : 990,
        "bournemouth" : 185,
        "brighton" : 166,
        "bristol" : 240,
        "buckinghamshire" : 216,
        "cambridgeshire" : 101,
        "cardiff" : 141,
        "cheshire" : 663,
        "chester" : 956,
        "cornwall" : 187,
        "cumbria" : 401,
        "derbyshire" : 410,
        "devon" : 142,
        "dorset" : 186,
        "durham" : 109,
        "east riding of yorkshire" : 614,
        "east sussex" : 299,
        "edinburgh" : 718,
        "essex" : 409,
        "glasgow" : 665,
        "glasgow" : 664,
        "gloucestershire" : 612,
        "hampshire" : 194,
        "hertfordshire" : 792,
        "high wycombe" : 215,
        "kent" : 387,
        "lancashire" : 273,
        "leicestershire" : 498,
        "lincolnshire" : 508,
        "liverpool" : 321,
        "london" : 59,
        "maidstone" : 535,
        "manchester" : 183,
        "merthyr tydfil" : 927,
        "nelson" : 649,
        "newcastle upon tyne" : 211,
        "norfolk" : 826,
        "north east lincolnshire" : 695,
        "north wales" : 892,
        "north yorkshire" : 438,
        "northamptonshire" : 625,
        "northern ireland" : 259,
        "nottinghamshire" : 191,
        "oxford" : 138,
        "peterborough" : 848,
        "portsmouth" : 193,
        "preston" : 1031,
        "scotland" : 87,
        "shetland" : 371,
        "shropshire" : 176,
        "somerset" : 253,
        "south kesteven" : 546,
        "south yorkshire" : 252,
        "southampton" : 699,
        "staffordshire" : 386,
        "stirlingshire" : 847,
        "suffolk" : 536,
        "surrey" : 403,
        "teesside" : 490,
        "wales" : 928,
        "wales" : 327,
        "warwickshire" : 257,
        "west midlands" : 134,
        "west sussex" : 241,
        "west yorkshire" : 221,
        "wiltshire" : 416,
        "worcestershire" : 587,
        "york" : 849,
        "alabama" : 1,
        "alaska" : 2,
        "all" : 942,
        "arizona" : 3,
        "arkansas" : 4,
        "california" : 5,
        "colorado" : 6,
        "connecticut" : 7,
        "delaware" : 8,
        "denial" : 492,
        "district of columbia" : 9,
        "florida" : 10,
        "georgia" : 11,
        "guam" : 717,
        "hawaii" : 12,
        "idaho" : 13,
        "illinois" : 14,
        "indiana" : 15,
        "iowa" : 16,
        "kansas" : 17,
        "kentucky" : 18,
        "louisiana" : 19,
        "maine" : 20,
        "marianas pacifica" : 875,
        "maryland" : 21,
        "massachusetts" : 22,
        "michigan" : 23,
        "minnesota" : 24,
        "mississippi" : 25,
        "missouri" : 26,
        "montana" : 27,
        "nebraska" : 28,
        "nevada" : 29,
        "new hampshire" : 30,
        "new jersey" : 31,
        "new mexico" : 32,
        "new york" : 33,
        "north carolina" : 34,
        "north dakota" : 35,
        "ohio" : 36,
        "oklahoma" : 37,
        "oregon" : 38,
        "pennsylvania" : 39,
        "puerto rico" : 1032,
        "rhode island" : 40,
        "south carolina" : 41,
        "south dakota" : 42,
        "tennessee" : 43,
        "texas" : 44,
        "us" : 943,
        "utah" : 45,
        "vermont" : 46,
        "virginia" : 47,
        "washington" : 48,
        "west virginia" : 49,
        "wisconsin" : 50,
        "wyoming" : 51,
        "montevideo" : 84,
        "tashkent" : 623,
        "merida" : 894,
        "caracas" : 439,
        "da nang" : 733,
        "hanoi" : 225,
        "ho chi minh city" : 226,
        "vi&#7879;t tr&#236;" : 867,
        "world wide web" : 918,
        "abertawe (swansea)" : 1007,
        "blaenau gwent" : 1002,
        "bro morgannwg (vale of glamorgan)" : 1004,
        "caerdydd (cardiff)" : 998,
        "caerffili (caerphilly)" : 996,
        "casnewydd (newport)" : 1000,
        "castell nedd a phort talbot (neath and port talbot)" : 1006,
        "ceredigion" : 1010,
        "conwy" : 1013,
        "gwynedd" : 1011,
        "merthyr tudful" : 999,
        "pen -y-bont a&#39;r ogwr (bridgend and ogmore)" : 1005,
        "powys" : 1017,
        "rhondda cynon taf" : 997,
        "sir benfro (pembrokeshire)" : 1009,
        "sir ddinbych (denbighshire)" : 1014,
        "sir fynwy (monmouthshire)" : 1003,
        "sir gaerfyrddin (carmarthenshire)" : 1008,
        "sir y fflint (flintshire)" : 1015,
        "torfaen" : 1001,
        "wrecsam (wrexham)" : 1016,
        "ynys m&#244;n (anglesey)" : 1012,
        "dc" : 846,
        "bel" : 949,
        "warwickshire" : 964,
        "nigeria" : 785,
        "world wide web" : 721,
        "mactopia" : 902,
        "philippine" : 915,
        "johor bahru" : 977,
        "kuala lumpur" : 239,
        "kuching" : 667,
        "penang" : 853,
        "sabah" : 581,
        "sarawak" : 951,
        "selangor" : 532,
        "yangon/rangoon" : 881,
        "panama city" : 837,
        "anotherprovince" : 832,
        "mystate" : 888,
        "testprovince" : 831 }

    def shows(self,irc,msg,args):
        # get username and place to use
        user = args[0]
        place = ' '.join(args[1:])

        # construct the feed url
        url = 'http://www.triv.org.uk/~mavit/upcomingscrobbler/?' + \
            'last_fm_user=%s;state_id=%s;format=atom'

        # figure out the place code
        place_code = Upcoming.places.get(place.lower().strip())
        if place_code == None:
            irc.reply("sorry i don't know where %s is" % place)
            return

        # get the shows
        feed = feedparser.parse(url % (user, place_code))
        shows = []
        for entry in feed.entries:
            shows.append(entry.title.encode('ascii', 'ignore') + ' [' + 
                entry.link + ']')

        # and display!
        if len(shows) > 0: 
            irc.reply(' ; '.join(shows))
        else:
            irc.reply("d'oh I don't know of any appropriate shows :(") 

Class = Upcoming
