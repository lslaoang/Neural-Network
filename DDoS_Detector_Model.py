#!/usr/bin/python

from math import exp
def Logistic (x) : 
    return (1/(1+exp(-x))) 

def Probability (x) : 
    if x < 0 :
        return 0
    elif x > 1 :
        return 1
    else : 
        return x

def expression (duration, protocol_type, service, flag, src_bytes, dst_bytes, land, wrong_fragment, urgent, count, srv_count, serror_rate, srv_serror_rate, rerror_rate, srv_rerror_rate, same_srv_rate, diff_srv_rate) : 

    scaled_duration=2*(duration-0)/(20-0)-1
    scaled_protocol_type=2*(protocol_type-0)/(2-0)-1
    scaled_service=2*(service-0)/(65-0)-1
    scaled_flag=2*(flag-2)/(9-2)-1
    scaled_src_bytes=2*(src_bytes-0)/(54540-0)-1
    scaled_dst_bytes=2*(dst_bytes-0)/(8315-0)-1
    scaled_land=2*(land-0)/(1-0)-1
    scaled_wrong_fragment=2*(wrong_fragment-0)/(3-0)-1
    scaled_urgent=2*(urgent-0)/(0-0)-1
    scaled_count=2*(count-1)/(511-1)-1
    scaled_srv_count=2*(srv_count-1)/(511-1)-1
    scaled_serror_rate=2*(serror_rate-0)/(1-0)-1
    scaled_srv_serror_rate=2*(srv_serror_rate-0)/(1-0)-1
    scaled_rerror_rate=2*(rerror_rate-0)/(1-0)-1
    scaled_srv_rerror_rate=2*(srv_rerror_rate-0)/(1-0)-1
    scaled_same_srv_rate=2*(same_srv_rate-0)/(1-0)-1
    scaled_diff_srv_rate=2*(diff_srv_rate-0)/(1-0)-1
    y_1_1=Logistic(0.335876
    +0.511047*scaled_duration
    +0.86145*scaled_protocol_type
    -0.0217285*scaled_service
    +0.736206*scaled_flag
    -0.699707*scaled_src_bytes
    +0.605042*scaled_dst_bytes
    +0.167542*scaled_land
    +0.646362*scaled_wrong_fragment
    -0.0790405*scaled_urgent
    +0.334167*scaled_count
    +0.273438*scaled_srv_count
    +0.249939*scaled_serror_rate
    -0.0556641*scaled_srv_serror_rate
    -0.0314331*scaled_rerror_rate
    -0.364746*scaled_srv_rerror_rate
    -0.767029*scaled_same_srv_rate
    +0.200134*scaled_diff_srv_rate)
    y_1_2=Logistic(0.356323
    +0.697876*scaled_duration
    +0.292908*scaled_protocol_type
    -0.500916*scaled_service
    -0.644775*scaled_flag
    +0.0179443*scaled_src_bytes
    +0.370483*scaled_dst_bytes
    +0.187988*scaled_land
    -0.582092*scaled_wrong_fragment
    +0.757996*scaled_urgent
    -0.583496*scaled_count
    -0.900757*scaled_srv_count
    +0.993591*scaled_serror_rate
    -0.268127*scaled_srv_serror_rate
    -0.493896*scaled_rerror_rate
    -0.542725*scaled_srv_rerror_rate
    -0.941772*scaled_same_srv_rate
    -0.937134*scaled_diff_srv_rate)
    y_1_3=Logistic(0.113831
    +0.304626*scaled_duration
    -0.913025*scaled_protocol_type
    -0.481628*scaled_service
    +0.360535*scaled_flag
    -0.990112*scaled_src_bytes
    -0.22052*scaled_dst_bytes
    -0.417908*scaled_land
    +0.0461426*scaled_wrong_fragment
    -0.57959*scaled_urgent
    +0.852661*scaled_count
    -0.672668*scaled_srv_count
    +0.279724*scaled_serror_rate
    -0.778076*scaled_srv_serror_rate
    -0.788757*scaled_rerror_rate
    -0.846252*scaled_srv_rerror_rate
    -0.480408*scaled_same_srv_rate
    -0.932495*scaled_diff_srv_rate)
    y_1_4=Logistic(-0.189148
    +0.449585*scaled_duration
    -0.163574*scaled_protocol_type
    -0.960938*scaled_service
    +0.52417*scaled_flag
    +0.242249*scaled_src_bytes
    -0.788513*scaled_dst_bytes
    -0.997253*scaled_land
    -0.676147*scaled_wrong_fragment
    +0.89978*scaled_urgent
    +0.681946*scaled_count
    +0.421875*scaled_srv_count
    -0.90564*scaled_serror_rate
    +0.945801*scaled_srv_serror_rate
    +0.147217*scaled_rerror_rate
    +0.189209*scaled_srv_rerror_rate
    +0.385071*scaled_same_srv_rate
    +0.0494385*scaled_diff_srv_rate)
    y_1_5=Logistic(-0.352722
    +0.0411987*scaled_duration
    -0.582642*scaled_protocol_type
    +0.254639*scaled_service
    -0.0735474*scaled_flag
    +0.116699*scaled_src_bytes
    -0.341919*scaled_dst_bytes
    +0.509338*scaled_land
    -0.905029*scaled_wrong_fragment
    +0.223267*scaled_urgent
    +0.271973*scaled_count
    +0.558594*scaled_srv_count
    -0.799866*scaled_serror_rate
    -0.628052*scaled_srv_serror_rate
    -0.234436*scaled_rerror_rate
    -0.737183*scaled_srv_rerror_rate
    -0.479248*scaled_same_srv_rate
    -0.854797*scaled_diff_srv_rate)
    y_1_6=Logistic(0.134644
    -0.595032*scaled_duration
    +0.396545*scaled_protocol_type
    -0.54126*scaled_service
    -0.171326*scaled_flag
    +0.0481567*scaled_src_bytes
    +0.404846*scaled_dst_bytes
    +0.280396*scaled_land
    +0.843445*scaled_wrong_fragment
    +0.506409*scaled_urgent
    +0.698181*scaled_count
    -0.131348*scaled_srv_count
    +0.255798*scaled_serror_rate
    +0.991699*scaled_srv_serror_rate
    -0.686279*scaled_rerror_rate
    -0.906555*scaled_srv_rerror_rate
    -0.488159*scaled_same_srv_rate
    -0.00140381*scaled_diff_srv_rate)
    y_1_7=Logistic(-0.731628
    +0.40094*scaled_duration
    -0.218201*scaled_protocol_type
    -0.509583*scaled_service
    -0.748474*scaled_flag
    +0.985901*scaled_src_bytes
    +0.693298*scaled_dst_bytes
    -0.0519409*scaled_land
    +0.727661*scaled_wrong_fragment
    +0.733154*scaled_urgent
    +0.756958*scaled_count
    +0.34491*scaled_srv_count
    +0.26178*scaled_serror_rate
    +0.491333*scaled_srv_serror_rate
    +0.794861*scaled_rerror_rate
    -0.889893*scaled_srv_rerror_rate
    +0.88031*scaled_same_srv_rate
    -0.758789*scaled_diff_srv_rate)
    y_1_8=Logistic(0.686157
    -0.857727*scaled_duration
    -0.72113*scaled_protocol_type
    -0.279297*scaled_service
    +0.741394*scaled_flag
    +0.936707*scaled_src_bytes
    +0.691101*scaled_dst_bytes
    -0.930054*scaled_land
    +0.0179443*scaled_wrong_fragment
    +0.88855*scaled_urgent
    +0.229553*scaled_count
    +0.0577393*scaled_srv_count
    +0.889709*scaled_serror_rate
    +0.833923*scaled_srv_serror_rate
    +0.511841*scaled_rerror_rate
    -0.546753*scaled_srv_rerror_rate
    +0.183289*scaled_same_srv_rate
    -0.108032*scaled_diff_srv_rate)
    y_1_9=Logistic(0.384644
    -0.895935*scaled_duration
    +0.192566*scaled_protocol_type
    +0.670227*scaled_service
    +0.557678*scaled_flag
    +0.284424*scaled_src_bytes
    -0.114868*scaled_dst_bytes
    +0.895569*scaled_land
    +0.960449*scaled_wrong_fragment
    +0.874756*scaled_urgent
    -0.387329*scaled_count
    +0.533875*scaled_srv_count
    -0.365967*scaled_serror_rate
    -0.0634766*scaled_srv_serror_rate
    -0.362854*scaled_rerror_rate
    -0.5401*scaled_srv_rerror_rate
    -0.02948*scaled_same_srv_rate
    -0.756592*scaled_diff_srv_rate)
    y_1_10=Logistic(-0.213196
    -0.259033*scaled_duration
    +0.112793*scaled_protocol_type
    +0.332642*scaled_service
    +0.552795*scaled_flag
    -0.403992*scaled_src_bytes
    -0.673096*scaled_dst_bytes
    +0.637756*scaled_land
    +0.940063*scaled_wrong_fragment
    -0.906738*scaled_urgent
    -0.840759*scaled_count
    -0.733704*scaled_srv_count
    -0.615479*scaled_serror_rate
    +0.648254*scaled_srv_serror_rate
    +0.192017*scaled_rerror_rate
    -0.0154419*scaled_srv_rerror_rate
    -0.950562*scaled_same_srv_rate
    +0.385803*scaled_diff_srv_rate)
    y_1_11=Logistic(0.208313
    -0.0284424*scaled_duration
    -0.187256*scaled_protocol_type
    -0.572998*scaled_service
    +0.580139*scaled_flag
    -0.0946655*scaled_src_bytes
    +0.258423*scaled_dst_bytes
    -0.835022*scaled_land
    +0.691345*scaled_wrong_fragment
    -0.0563965*scaled_urgent
    -0.0151978*scaled_count
    -0.408569*scaled_srv_count
    -0.79126*scaled_serror_rate
    -0.838501*scaled_srv_serror_rate
    -0.459229*scaled_rerror_rate
    +0.736145*scaled_srv_rerror_rate
    +0.0125732*scaled_same_srv_rate
    -0.99115*scaled_diff_srv_rate)
    y_1_12=Logistic(0.304321
    +0.282532*scaled_duration
    -0.399658*scaled_protocol_type
    +0.349487*scaled_service
    -0.385498*scaled_flag
    -0.578491*scaled_src_bytes
    -0.224426*scaled_dst_bytes
    +0.645264*scaled_land
    -0.529968*scaled_wrong_fragment
    +0.00579834*scaled_urgent
    +0.43396*scaled_count
    +0.846558*scaled_srv_count
    +0.106323*scaled_serror_rate
    -0.932068*scaled_srv_serror_rate
    +0.260132*scaled_rerror_rate
    +0.552917*scaled_srv_rerror_rate
    +0.764771*scaled_same_srv_rate
    -0.236145*scaled_diff_srv_rate)
    y_1_13=Logistic(0.146667
    -0.994507*scaled_duration
    +0.965149*scaled_protocol_type
    +0.804749*scaled_service
    -0.851501*scaled_flag
    +0.473877*scaled_src_bytes
    +0.594849*scaled_dst_bytes
    -0.560303*scaled_land
    -0.214966*scaled_wrong_fragment
    -0.399658*scaled_urgent
    +0.126709*scaled_count
    +0.0516357*scaled_srv_count
    +0.502136*scaled_serror_rate
    -0.737*scaled_srv_serror_rate
    -0.721191*scaled_rerror_rate
    -0.570923*scaled_srv_rerror_rate
    +0.107056*scaled_same_srv_rate
    +0.521729*scaled_diff_srv_rate)
    y_1_14=Logistic(-0.572693
    +0.776245*scaled_duration
    -0.0117798*scaled_protocol_type
    -0.792114*scaled_service
    +0.0866699*scaled_flag
    -0.476379*scaled_src_bytes
    +0.933167*scaled_dst_bytes
    +0.721802*scaled_land
    +0.767883*scaled_wrong_fragment
    -0.997742*scaled_urgent
    +0.35614*scaled_count
    -0.400757*scaled_srv_count
    +0.52887*scaled_serror_rate
    -0.956543*scaled_srv_serror_rate
    +0.748413*scaled_rerror_rate
    -0.589966*scaled_srv_rerror_rate
    +0.528198*scaled_same_srv_rate
    -0.433044*scaled_diff_srv_rate)
    y_1_15=Logistic(-0.835815
    -0.448669*scaled_duration
    -0.104492*scaled_protocol_type
    +0.220032*scaled_service
    +0.553528*scaled_flag
    +0.498047*scaled_src_bytes
    +0.230774*scaled_dst_bytes
    +0.129333*scaled_land
    +0.755981*scaled_wrong_fragment
    +0.0723267*scaled_urgent
    -0.954895*scaled_count
    +0.829102*scaled_srv_count
    -0.0333862*scaled_serror_rate
    +0.29541*scaled_srv_serror_rate
    -0.544922*scaled_rerror_rate
    +0.42749*scaled_srv_rerror_rate
    +0.487183*scaled_same_srv_rate
    -0.615723*scaled_diff_srv_rate)
    y_1_16=Logistic(0.44397
    +0.0733643*scaled_duration
    -0.425049*scaled_protocol_type
    +0.45459*scaled_service
    -0.998474*scaled_flag
    +0.786865*scaled_src_bytes
    -0.798035*scaled_dst_bytes
    -0.506165*scaled_land
    +0.4552*scaled_wrong_fragment
    -0.284607*scaled_urgent
    -0.463684*scaled_count
    +0.166321*scaled_srv_count
    +0.305481*scaled_serror_rate
    -0.122131*scaled_srv_serror_rate
    -0.0404663*scaled_rerror_rate
    +0.0123901*scaled_srv_rerror_rate
    -0.122498*scaled_same_srv_rate
    +0.460205*scaled_diff_srv_rate)
    y_1_17=Logistic(0.430542
    -0.394897*scaled_duration
    -0.89856*scaled_protocol_type
    -0.276428*scaled_service
    -0.989197*scaled_flag
    -0.773804*scaled_src_bytes
    +0.734558*scaled_dst_bytes
    -0.411438*scaled_land
    +0.361206*scaled_wrong_fragment
    +0.624268*scaled_urgent
    -0.663025*scaled_count
    -0.0422363*scaled_srv_count
    -0.975159*scaled_serror_rate
    +0.417114*scaled_srv_serror_rate
    -0.686035*scaled_rerror_rate
    -0.160889*scaled_srv_rerror_rate
    +0.307068*scaled_same_srv_rate
    +0.701599*scaled_diff_srv_rate)
    y_1_18=Logistic(-0.663025
    -0.66748*scaled_duration
    +0.565613*scaled_protocol_type
    -0.567444*scaled_service
    -0.543762*scaled_flag
    -0.458069*scaled_src_bytes
    -0.276245*scaled_dst_bytes
    +0.134216*scaled_land
    +0.217407*scaled_wrong_fragment
    +0.476257*scaled_urgent
    -0.181702*scaled_count
    -0.494141*scaled_srv_count
    +0.0940552*scaled_serror_rate
    +0.000671387*scaled_srv_serror_rate
    +0.395264*scaled_rerror_rate
    +0.484375*scaled_srv_rerror_rate
    +0.549683*scaled_same_srv_rate
    -0.0986938*scaled_diff_srv_rate)
    y_1_19=Logistic(0.565918
    -0.673218*scaled_duration
    -0.958984*scaled_protocol_type
    +0.125854*scaled_service
    +0.5354*scaled_flag
    +0.274353*scaled_src_bytes
    -0.725342*scaled_dst_bytes
    -0.737976*scaled_land
    +0.416199*scaled_wrong_fragment
    +0.361633*scaled_urgent
    -0.968994*scaled_count
    +0.317444*scaled_srv_count
    -0.860291*scaled_serror_rate
    -0.0679321*scaled_srv_serror_rate
    +0.866455*scaled_rerror_rate
    -0.137756*scaled_srv_rerror_rate
    -0.72229*scaled_same_srv_rate
    -0.576355*scaled_diff_srv_rate)
    y_1_20=Logistic(0.00720215
    -0.402283*scaled_duration
    +0.586548*scaled_protocol_type
    -0.013855*scaled_service
    +0.746887*scaled_flag
    +0.41333*scaled_src_bytes
    +0.0866089*scaled_dst_bytes
    +0.493286*scaled_land
    -0.339111*scaled_wrong_fragment
    -0.00585938*scaled_urgent
    -0.510986*scaled_count
    +0.511475*scaled_srv_count
    +0.949158*scaled_serror_rate
    +0.0419922*scaled_srv_serror_rate
    -0.216736*scaled_rerror_rate
    -0.211426*scaled_srv_rerror_rate
    +0.220825*scaled_same_srv_rate
    +0.171997*scaled_diff_srv_rate)
    y_2_1=Logistic(-0.203613
    -0.175659*y_1_1
    +0.0322876*y_1_2
    +0.547913*y_1_3
    +0.538696*y_1_4
    +0.0854492*y_1_5
    -0.507812*y_1_6
    +0.317444*y_1_7
    +0.145691*y_1_8
    +0.427734*y_1_9
    -0.755127*y_1_10
    -0.0882568*y_1_11
    -0.768738*y_1_12
    +0.287903*y_1_13
    +0.145569*y_1_14
    +0.270081*y_1_15
    -0.536865*y_1_16
    +0.206909*y_1_17
    +0.939331*y_1_18
    -0.947083*y_1_19
    -0.826782*y_1_20)
    y_2_2=Logistic(0.248535
    -0.743774*y_1_1
    +0.906006*y_1_2
    +0.815979*y_1_3
    +0.874329*y_1_4
    -0.76416*y_1_5
    -0.162598*y_1_6
    +0.0869751*y_1_7
    +0.838684*y_1_8
    +0.0928345*y_1_9
    +0.770447*y_1_10
    -0.486206*y_1_11
    -0.334717*y_1_12
    +0.936523*y_1_13
    +0.335327*y_1_14
    +0.332214*y_1_15
    -0.731262*y_1_16
    +0.156921*y_1_17
    -0.0393677*y_1_18
    -0.539795*y_1_19
    +0.282898*y_1_20)
    y_2_3=Logistic(0.689453
    -0.670837*y_1_1
    -0.618103*y_1_2
    -0.341309*y_1_3
    -0.528442*y_1_4
    -0.741394*y_1_5
    -0.245667*y_1_6
    -0.906067*y_1_7
    +0.402649*y_1_8
    +0.0712891*y_1_9
    +0.549255*y_1_10
    +0.858032*y_1_11
    -0.879211*y_1_12
    +0.514099*y_1_13
    -0.457458*y_1_14
    +0.573486*y_1_15
    +0.908264*y_1_16
    -0.708069*y_1_17
    -0.0360107*y_1_18
    -0.483459*y_1_19
    +0.0383911*y_1_20)
    y_2_4=Logistic(0.277161
    -0.88031*y_1_1
    +0.000793457*y_1_2
    -0.123474*y_1_3
    -0.543152*y_1_4
    -0.200745*y_1_5
    +0.404236*y_1_6
    +0.0471191*y_1_7
    +0.681152*y_1_8
    -0.718933*y_1_9
    -0.595703*y_1_10
    -0.0200195*y_1_11
    +0.275146*y_1_12
    -0.252319*y_1_13
    -0.0182495*y_1_14
    -0.852295*y_1_15
    -0.424377*y_1_16
    +0.923584*y_1_17
    +0.756958*y_1_18
    -0.692749*y_1_19
    -0.542786*y_1_20)
    y_2_5=Logistic(0.748474
    -0.779236*y_1_1
    -0.9422*y_1_2
    -0.0912476*y_1_3
    +0.897705*y_1_4
    +0.421875*y_1_5
    +0.0274658*y_1_6
    +0.722595*y_1_7
    +0.963623*y_1_8
    -0.325684*y_1_9
    -0.998596*y_1_10
    +0.360535*y_1_11
    +0.108765*y_1_12
    +0.846985*y_1_13
    -0.695984*y_1_14
    -0.942566*y_1_15
    +0.00469971*y_1_16
    +0.797058*y_1_17
    -0.252625*y_1_18
    -0.774414*y_1_19
    -0.131531*y_1_20)
    y_2_6=Logistic(-0.488953
    +0.45874*y_1_1
    -0.777222*y_1_2
    -0.590881*y_1_3
    +0.515381*y_1_4
    -0.100891*y_1_5
    -0.454285*y_1_6
    +0.496765*y_1_7
    -0.88147*y_1_8
    +0.386108*y_1_9
    -0.488037*y_1_10
    -0.632996*y_1_11
    -0.951904*y_1_12
    +0.433044*y_1_13
    -0.507263*y_1_14
    +0.173096*y_1_15
    -0.955017*y_1_16
    -0.78302*y_1_17
    +0.758667*y_1_18
    -0.302307*y_1_19
    -0.0234375*y_1_20)
    y_2_7=Logistic(-0.511902
    +0.00164795*y_1_1
    +0.0380859*y_1_2
    +0.0325317*y_1_3
    +0.233032*y_1_4
    +0.594727*y_1_5
    -0.924011*y_1_6
    +0.56488*y_1_7
    -0.595398*y_1_8
    -0.346985*y_1_9
    -0.454773*y_1_10
    +0.13501*y_1_11
    +0.0305176*y_1_12
    +0.957764*y_1_13
    +0.509338*y_1_14
    -0.669617*y_1_15
    +0.0133667*y_1_16
    +0.806091*y_1_17
    +0.0621948*y_1_18
    -0.0866699*y_1_19
    +0.934509*y_1_20)
    y_2_8=Logistic(0.849243
    -0.936401*y_1_1
    +0.864014*y_1_2
    +0.174622*y_1_3
    +0.981445*y_1_4
    +0.722534*y_1_5
    +0.880798*y_1_6
    -0.337158*y_1_7
    +0.342102*y_1_8
    -0.159546*y_1_9
    -0.0997925*y_1_10
    -0.432556*y_1_11
    -0.506165*y_1_12
    +0.527344*y_1_13
    -0.801514*y_1_14
    +0.240295*y_1_15
    -0.161377*y_1_16
    +0.203186*y_1_17
    +0.637878*y_1_18
    +0.728271*y_1_19
    -0.664978*y_1_20)
    y_2_9=Logistic(0.696533
    +0.620361*y_1_1
    -0.837402*y_1_2
    +0.578247*y_1_3
    +0.253845*y_1_4
    -0.68988*y_1_5
    -0.659424*y_1_6
    +0.30658*y_1_7
    -0.729248*y_1_8
    +0.688843*y_1_9
    +0.810425*y_1_10
    +0.395447*y_1_11
    -0.440552*y_1_12
    +0.00482178*y_1_13
    +0.773376*y_1_14
    -0.59729*y_1_15
    -0.0373535*y_1_16
    +0.179871*y_1_17
    -0.886414*y_1_18
    +0.727295*y_1_19
    +0.128723*y_1_20)
    y_2_10=Logistic(-0.265076
    +0.870667*y_1_1
    +0.443115*y_1_2
    -0.741394*y_1_3
    -0.201538*y_1_4
    -0.534973*y_1_5
    +0.871765*y_1_6
    -0.361389*y_1_7
    +0.758789*y_1_8
    +0.990356*y_1_9
    +0.955688*y_1_10
    -0.229797*y_1_11
    +0.12384*y_1_12
    +0.884766*y_1_13
    -0.505127*y_1_14
    +0.910767*y_1_15
    +0.15033*y_1_16
    -0.706665*y_1_17
    +0.309326*y_1_18
    -0.164062*y_1_19
    +0.804871*y_1_20)
    y_2_11=Logistic(0.434326
    -0.610779*y_1_1
    -0.361816*y_1_2
    +0.619568*y_1_3
    +0.28241*y_1_4
    -0.903137*y_1_5
    -0.627563*y_1_6
    -0.994873*y_1_7
    -0.11969*y_1_8
    -0.51886*y_1_9
    +0.361877*y_1_10
    +0.582764*y_1_11
    +0.591736*y_1_12
    -0.232056*y_1_13
    -0.0234375*y_1_14
    -0.901367*y_1_15
    +0.608765*y_1_16
    +0.0890503*y_1_17
    +0.697205*y_1_18
    -0.517273*y_1_19
    -0.97467*y_1_20)
    y_2_12=Logistic(0.511536
    -0.723511*y_1_1
    -0.385254*y_1_2
    +0.789368*y_1_3
    -0.569214*y_1_4
    -0.189392*y_1_5
    +0.359375*y_1_6
    +0.846741*y_1_7
    +0.388977*y_1_8
    -0.466553*y_1_9
    -0.566223*y_1_10
    +0.789001*y_1_11
    -0.618103*y_1_12
    -0.853943*y_1_13
    -0.330383*y_1_14
    +0.317566*y_1_15
    -0.283264*y_1_16
    +0.493408*y_1_17
    -0.767944*y_1_18
    +0.836426*y_1_19
    +0.483032*y_1_20)
    y_2_13=Logistic(-0.598267
    +0.358154*y_1_1
    -0.513123*y_1_2
    -0.30072*y_1_3
    +0.488342*y_1_4
    +0.177551*y_1_5
    +0.935791*y_1_6
    +0.197998*y_1_7
    -0.24353*y_1_8
    +0.177429*y_1_9
    -0.769836*y_1_10
    -0.688293*y_1_11
    -0.211914*y_1_12
    -0.125244*y_1_13
    -0.968933*y_1_14
    +0.421631*y_1_15
    -0.653503*y_1_16
    -0.742004*y_1_17
    +0.538391*y_1_18
    -0.5672*y_1_19
    +0.201843*y_1_20)
    y_2_14=Logistic(-0.439514
    -0.580017*y_1_1
    +0.237183*y_1_2
    +0.991699*y_1_3
    +0.928955*y_1_4
    +0.0570068*y_1_5
    +0.227661*y_1_6
    +0.929504*y_1_7
    +0.548706*y_1_8
    -0.58197*y_1_9
    -0.0751953*y_1_10
    -0.827454*y_1_11
    -0.211731*y_1_12
    -0.124939*y_1_13
    -0.219482*y_1_14
    +0.663513*y_1_15
    -0.0736694*y_1_16
    +0.272644*y_1_17
    +0.21875*y_1_18
    +0.256348*y_1_19
    -0.97699*y_1_20)
    y_2_15=Logistic(-0.435669
    -0.0222168*y_1_1
    -0.0596924*y_1_2
    -0.501831*y_1_3
    +0.327209*y_1_4
    +0.815491*y_1_5
    +0.973938*y_1_6
    +0.979492*y_1_7
    +0.468384*y_1_8
    -0.359497*y_1_9
    -0.258179*y_1_10
    -0.0177002*y_1_11
    +0.43512*y_1_12
    +0.13147*y_1_13
    -0.853638*y_1_14
    +0.983948*y_1_15
    +0.241394*y_1_16
    +0.90741*y_1_17
    +0.347229*y_1_18
    +0.455505*y_1_19
    -0.376282*y_1_20)
    y_3_1=Logistic(0.310974
    +0.661194*y_2_1
    +0.412659*y_2_2
    -0.362427*y_2_3
    +0.867676*y_2_4
    +0.434204*y_2_5
    -0.951355*y_2_6
    -0.991394*y_2_7
    -0.516296*y_2_8
    +0.699219*y_2_9
    -0.987854*y_2_10
    -0.450134*y_2_11
    +0.443848*y_2_12
    +0.430847*y_2_13
    +0.891602*y_2_14
    -0.0423584*y_2_15)
    y_3_2=Logistic(-0.726929
    -0.78894*y_2_1
    +0.469666*y_2_2
    +0.299316*y_2_3
    +0.524231*y_2_4
    +0.116943*y_2_5
    -0.690918*y_2_6
    +0.504761*y_2_7
    -0.446594*y_2_8
    +0.643677*y_2_9
    -0.766479*y_2_10
    -0.825928*y_2_11
    -0.653625*y_2_12
    +0.475647*y_2_13
    +0.265503*y_2_14
    +0.0144043*y_2_15)
    y_3_3=Logistic(0.458313
    -0.0830688*y_2_1
    +0.583252*y_2_2
    +0.218201*y_2_3
    -0.870728*y_2_4
    -0.204834*y_2_5
    +0.0605469*y_2_6
    +0.0952759*y_2_7
    -0.362*y_2_8
    +0.650085*y_2_9
    -0.0499878*y_2_10
    +0.271118*y_2_11
    -0.0435791*y_2_12
    +0.0200195*y_2_13
    +0.274414*y_2_14
    -0.235474*y_2_15)
    y_3_4=Logistic(0.767517
    -0.361572*y_2_1
    -0.513123*y_2_2
    -0.743652*y_2_3
    +0.908813*y_2_4
    -0.647034*y_2_5
    -0.0368042*y_2_6
    +0.861938*y_2_7
    -0.695618*y_2_8
    -0.420105*y_2_9
    -0.11084*y_2_10
    +0.720703*y_2_11
    +0.447388*y_2_12
    -0.893738*y_2_13
    -0.895935*y_2_14
    -0.286255*y_2_15)
    y_3_5=Logistic(-0.503784
    +0.0516357*y_2_1
    -0.535278*y_2_2
    +0.623413*y_2_3
    +0.0460815*y_2_4
    +0.803345*y_2_5
    -0.709351*y_2_6
    -0.953186*y_2_7
    +0.639038*y_2_8
    +0.736328*y_2_9
    +0.454346*y_2_10
    +0.375122*y_2_11
    -0.925293*y_2_12
    -0.469482*y_2_13
    -0.321655*y_2_14
    +0.152771*y_2_15)
    y_3_6=Logistic(0.584473
    +0.899048*y_2_1
    +0.601868*y_2_2
    +0.126953*y_2_3
    +0.931335*y_2_4
    -0.461731*y_2_5
    +0.179565*y_2_6
    -0.697998*y_2_7
    +0.498047*y_2_8
    -0.886292*y_2_9
    -0.0252686*y_2_10
    +0.309509*y_2_11
    +0.425781*y_2_12
    +0.0930176*y_2_13
    -0.0906982*y_2_14
    +0.407654*y_2_15)
    y_3_7=Logistic(0.866699
    -0.760437*y_2_1
    -0.965942*y_2_2
    -0.578003*y_2_3
    +0.411743*y_2_4
    -0.421448*y_2_5
    +0.880066*y_2_6
    -0.0601196*y_2_7
    +0.756897*y_2_8
    +0.647949*y_2_9
    -0.0447388*y_2_10
    +0.0714111*y_2_11
    -0.329834*y_2_12
    -0.152344*y_2_13
    +0.94751*y_2_14
    +0.0895996*y_2_15)
    y_3_8=Logistic(0.322021
    +0.698547*y_2_1
    -0.802063*y_2_2
    -0.738647*y_2_3
    +0.0415649*y_2_4
    +0.823792*y_2_5
    +0.00549316*y_2_6
    +0.182861*y_2_7
    +0.560669*y_2_8
    -0.533752*y_2_9
    -0.67334*y_2_10
    +0.931213*y_2_11
    +0.809326*y_2_12
    -0.647522*y_2_13
    -0.568359*y_2_14
    +0.344788*y_2_15)
    y_3_9=Logistic(0.324097
    +0.71759*y_2_1
    +0.0808716*y_2_2
    +0.7453*y_2_3
    +0.332153*y_2_4
    +0.302795*y_2_5
    +0.782471*y_2_6
    -0.586365*y_2_7
    +0.574036*y_2_8
    -0.862671*y_2_9
    +0.695435*y_2_10
    -0.868164*y_2_11
    +0.926941*y_2_12
    -0.0808105*y_2_13
    -0.26123*y_2_14
    -0.895264*y_2_15)
    y_3_10=Logistic(-0.10907
    -0.195068*y_2_1
    -0.529053*y_2_2
    +0.572021*y_2_3
    -0.998291*y_2_4
    -0.577087*y_2_5
    -0.699097*y_2_6
    +0.424927*y_2_7
    -0.76886*y_2_8
    -0.0787354*y_2_9
    +0.593872*y_2_10
    -0.860962*y_2_11
    +0.438477*y_2_12
    +0.863586*y_2_13
    +0.234131*y_2_14
    +0.336121*y_2_15)
    y_4_1=Logistic(-0.0647583
    +0.785034*y_3_1
    +0.207153*y_3_2
    +0.28717*y_3_3
    -0.774292*y_3_4
    -0.779297*y_3_5
    +0.763916*y_3_6
    +0.669739*y_3_7
    +0.985596*y_3_8
    +0.0194702*y_3_9
    -0.269897*y_3_10)
    y_4_2=Logistic(0.890991
    -0.658447*y_3_1
    +0.75531*y_3_2
    -0.478699*y_3_3
    -0.709412*y_3_4
    -0.485779*y_3_5
    +0.0488281*y_3_6
    +0.429138*y_3_7
    -0.46582*y_3_8
    -0.113525*y_3_9
    -0.38855*y_3_10)
    y_4_3=Logistic(-0.261902
    -0.488892*y_3_1
    +0.560608*y_3_2
    +0.82489*y_3_3
    -0.762146*y_3_4
    -0.951294*y_3_5
    -0.534058*y_3_6
    +0.667908*y_3_7
    +0.6922*y_3_8
    -0.244873*y_3_9
    +0.0795898*y_3_10)
    y_4_4=Logistic(0.80365
    -0.172546*y_3_1
    -0.696045*y_3_2
    -0.176575*y_3_3
    +0.639465*y_3_4
    +0.403076*y_3_5
    -0.527649*y_3_6
    -0.801025*y_3_7
    +0.171814*y_3_8
    +0.92688*y_3_9
    +0.245789*y_3_10)
    y_4_5=Logistic(0.723206
    -0.571167*y_3_1
    -0.423096*y_3_2
    -0.69812*y_3_3
    -0.2724*y_3_4
    +0.323242*y_3_5
    -0.106689*y_3_6
    -0.814697*y_3_7
    +0.0830688*y_3_8
    -0.272156*y_3_9
    +0.801941*y_3_10)
    non_probabilistic_label=Logistic(-0.513184
    +0.912964*y_4_1
    -0.414124*y_4_2
    -0.467529*y_4_3
    +0.33844*y_4_4
    -0.642883*y_4_5)
    (label) = Probability(non_probabilistic_label)
    
    return label 