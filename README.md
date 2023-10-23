# ecomProductEmbeddingLoader
Reads a file of product IDs, computes vector embeddings using LangChain (based on the name) to be stored in Astra DB.

## Requirements
 - Account with [Astra DB](https://astra.datastax.com/).
 - Generate a token.
 - Download the SCB.
 - Create/fill-out `.env` file (see `.env_example`)

## schema
Keyspace: `ecommerce`
CQL Table definition:

```sql
CREATE TABLE product_vectors (
    product_id TEXT PRIMARY KEY,
    name TEXT,
    product_group TEXT,
    parent_id UUID,
    category_id UUID,
    images SET<TEXT>,
    product_vector vector<float,384>);

CREATE CUSTOM INDEX ON product_vectors(product_vector) USING 'StorageAttachedIndex';
```

## Functionality
Reads from the data/[product_ids.csv](data/product_ids.csv) file, generates embeddings using LangChain and the HuggingFace `all-MiniLM-L6-v2` sentence transformer. Loads embeddings into `product_vector` table in Astra DB.

## Output
```
DSA1121M, DataStax Astra "One Team" Long Sleeve Tee, [-0.12828106, 0.0911595, -0.05123979, 0.041872043, -0.010696648, -0.042400908, 0.013541876, 0.028344385, -0.031757925, -0.048159238, -0.0143808015, -0.021521732, 0.022061368, 0.0010908962, -0.00445854, -0.017649783, 0.0012698525, -0.05497383, 0.0038058152, -0.05738303, -0.030689018, -0.06980758, -0.009855664, 0.0459129, 0.033187788, -0.0032011361, -0.030323356, 0.013018566, -0.024780171, -0.13477555, -0.031757154, -0.025323676, 0.04573877, 0.122665875, -0.020512434, -0.046718642, 0.050697424, 0.07431821, -0.07190838, 0.04959432, 0.052959856, -0.07182941, -0.02651779, 0.02127486, -0.044687647, -0.0045170933, -0.119697146, 0.031502623, 0.06393135, 0.13211323, 0.020050332, -0.029622426, 0.035482693, 0.07843326, 0.0029373732, -0.009169235, -0.033201743, 0.014156842, -0.0037300526, -0.021947253, 0.098318696, -0.0399827, -0.062477533, -0.003982953, 0.05370842, -0.025560072, -0.049229857, 0.13305682, -0.03682456, 0.037582815, 0.050818197, -0.04528362, -0.053975597, 0.07205402, 0.050475527, 0.11209492, -0.0060483636, -0.0067837415, 0.021989131, 0.04574819, -0.05229753, -0.0023137482, -0.037799194, 0.069850534, -0.05263051, 0.101432964, -0.038325097, 0.018643817, -0.058988366, -0.048843157, -0.029273804, 0.07931474, 0.06675547, 0.019754995, -0.012714609, 0.060890187, 0.021766286, 0.017446864, 0.015995331, 0.0189985, -0.013207963, 0.03305, 0.012427895, 0.015050355, -0.04093009, -0.13204409, -0.03526449, -0.033478614, 0.059460375, -0.07057777, 5.1382574E-4, -0.019078732, -0.04717889, -0.054796055, -0.100971386, -0.020525314, -0.13453773, 0.05306184, -0.023042893, -0.020602345, 0.013213792, -0.006454958, -0.10438688, 0.031186529, 0.07973203, 0.0079892, 0.024518339, 1.3866929E-33, -0.013964732, 0.04194874, 0.008108536, 0.03700172, 0.07233341, -0.01677471, -0.011282754, -0.10701145, -0.09913037, 0.057469677, -0.055104382, 0.014418184, 0.007826463, 0.035289466, 0.014107688, -0.084076084, 0.01228236, 1.7590926E-4, -0.08488218, 0.011904588, -0.024415988, -0.012512333, 0.033488903, -0.04805186, -0.019239515, 0.02063535, -0.11106853, 0.007450389, 0.024936019, 0.026580598, -0.04043952, 0.026641646, -0.007218114, 0.052130967, -0.02792826, -0.06948612, -0.036497634, -0.014838626, 0.003706102, 0.07270272, 0.016123839, 0.014113162, -0.03058305, -0.020418173, -0.070631996, -0.051853653, 0.029575292, -0.024863794, 0.049117353, -0.05369889, 0.017121784, 0.02788029, -0.012669457, -0.028201066, 0.05226569, -0.046625353, 0.027293546, 0.03297922, 0.04988747, 0.030717855, -3.1636114E-4, 0.057238277, 0.024088811, 0.026382903, -0.03658029, 0.07099247, 0.074688345, -0.0626112, 0.065399244, -0.040395208, 0.005701385, 0.05165972, 0.043032486, 0.019983487, 0.05035135, 0.006586599, 0.031542793, 0.076449916, -0.025485553, -0.031392004, -0.06356821, -0.083924286, -0.007298202, 0.053036224, 0.015939271, -0.008379747, 0.038113378, -0.0438309, -0.06139312, 0.037626985, -0.09012226, -0.032868974, -0.011806652, -0.059325654, 0.049679678, -1.1305057E-33, 0.12392222, -0.022712396, 0.052024785, -0.027984656, 0.11518019, 0.025920156, 0.10190534, 0.09163093, 0.02492093, 0.0955827, 0.1098759, 0.02147502, -0.10245577, -0.007818765, 0.041207217, 0.096847996, 0.093758516, -0.036566224, -0.027443497, -0.050232697, 0.03678656, -0.06342057, 0.021539757, 0.10389469, -0.006626326, -0.008210247, 0.065437496, -0.05409399, -0.031596914, 0.0013363977, -0.0364998, -0.012909269, -0.011105978, -0.0072830752, -0.0053150905, -0.0048118243, 0.05224331, 0.11907376, 0.036398906, 3.9881712E-4, 0.007163071, -0.0099789165, -0.055986088, -0.0028383788, 0.042961378, -0.07710615, -0.080483824, 0.0014898821, -0.030184772, 0.040207062, 0.011260589, 0.00620204, 0.050260797, 0.0050185304, -0.0075070746, -5.4974126E-4, 0.019844307, 0.014314984, -0.10132302, 0.013932586, -0.003997444, -0.010421064, 0.010706773, -6.524287E-4, 0.05478795, 0.053754292, -0.011018024, -0.08360094, -0.10324705, 0.0782125, -0.058208454, -0.021775007, -0.03481282, 0.041962497, -0.0037493713, -0.07904612, -0.08100054, 0.064308934, 0.030283121, 0.087728165, -0.09454709, -0.02855172, 0.010005955, 0.025366195, 0.18483993, 0.028593553, 0.01562748, 0.1287155, -0.008192512, 0.058474988, -0.008502188, -0.053598996, 0.0081902165, 0.059492644, 0.056984123, -1.7241966E-8, -0.029972611, -0.010650358, 0.009776672, -0.024940735, 0.055130724, 0.035771713, -0.054123558, -0.04565081, 0.062665425, -0.0058652596, 0.04588764, -0.010536247, 0.03408485, -0.034140993, -0.045800604, -0.029557861, -0.048121452, -0.00816124, -0.031020738, -0.06663867, -0.005200036, 0.040860485, -0.023477217, -0.0033413128, -0.0073512956, 0.011512698, -0.04188342, 0.07888328, 0.0049446896, -0.07031161, 0.026609086, -0.015323752, 0.011051029, -0.040054485, 0.09784346, -0.0396561, 0.06608354, -0.011109917, 0.034592897, 0.066440985, -0.008927181, 0.0018028528, -0.026357146, 0.009545543, 0.037641875, 0.018215982, -0.01994085, -0.02106611, -0.08077866, -0.017160198, 0.06716771, -0.055346414, -0.038624015, 0.0422528, 0.017767554, -0.013818962, -0.04519948, -0.009713665, -0.035597764, 0.044979263, -0.013873211, -0.043236945, 0.01857768, 0.023844365]
LS534M, Go Away Annotation T-Shirt, [-0.03660766, 0.17068991, -6.797607E-5, 0.013803028, 0.15503922, 0.032511145, 0.115351945, -0.017074786, 0.023120396, -0.05360752, 0.036346875, 0.0032500543, 0.018614942, 0.045027517, 0.024062198, 0.053020734, 0.016931456, 0.014445507, -0.035558086, -0.05505228, -0.023492629, 0.05552709, 0.062397197, 0.077756494, -0.011309487, -0.055834576, -0.052176848, -0.028794745, -0.014988517, -0.009281843, -0.038120147, 0.089498796, -0.00303338, 0.005256841, -0.030212406, -0.039765272, 0.019952439, 0.10438376, 0.023941888, 0.028155962, 3.4310843E-4, -0.0967887, -0.06790676, 0.030878887, 0.037792288, 0.09115847, -0.0062833736, 0.01430361, -0.06345592, 0.09629193, 0.030418955, -0.083409004, -0.010060576, -0.054874144, 0.013269879, 0.035466265, 0.09462886, -0.04209471, -0.057360426, 0.024775242, 0.08067586, -0.052106686, -0.07633911, 0.061823133, 0.078377634, -1.0794598E-4, 0.046955884, 0.038856234, -0.026526207, 0.017160747, 0.05961203, -0.018434992, 0.026958222, 0.10224336, 0.039012995, 0.071185544, 0.033842824, -0.017657487, 0.035979524, -0.024246724, -0.05672811, 0.04518434, 0.0540871, -0.025070813, -0.0489911, 0.02661993, -0.016531084, -0.009302283, 0.04652628, -0.0039611068, -0.04966337, 0.00790944, 0.05230786, 0.01719059, -0.021396386, -0.023883056, -0.12156989, -0.015862191, -0.06332286, 0.11951203, 0.019032124, 0.03714531, 0.03172512, 0.037318863, 0.011786686, -0.061692208, -0.006837919, 0.0109119, 0.06441315, -1.0854246E-4, -0.021548321, 0.022913039, -0.022012789, -0.0053936755, -0.0072935666, -0.034773197, 0.08505519, 0.09958001, 0.08454777, -0.029302385, -0.028560756, 0.01265986, -0.07981411, 0.024768267, 0.015277899, -0.038033754, -0.02135915, -8.169714E-35, 0.07342774, 0.055485386, -0.044437446, 0.07528237, 0.022740195, -0.023127846, -0.040902987, -0.11677126, 0.016573023, -0.0035242857, 0.030685017, -0.04540893, -0.019007904, 0.042952802, -0.006942158, -5.430004E-4, -0.0010199485, -0.014377479, -0.04855833, -0.054463774, -0.0045386837, 0.11137218, -0.0020051252, -0.060865723, -0.022814598, 0.10072957, 0.008342984, -0.06910482, -0.03674017, 0.031957608, 0.045062914, -0.013123019, 0.04758635, 0.0076980563, -0.0037114166, -0.048612863, -0.033930555, 0.0023533446, 0.03030089, -0.0015425636, 0.06415615, 0.046027504, -0.0019379065, 0.010192939, 0.013443835, 0.002868605, 0.08180649, 0.012772166, 0.014696793, -0.0145626515, 0.065605946, -0.010436503, -0.0127188675, -0.13016364, -0.088924564, -0.07852744, -0.0074292803, 0.009874483, 0.029230243, -0.07343814, -0.004822139, 0.034370717, 0.06509724, -0.003956874, -0.019315725, 3.1117586E-4, -0.058143057, -0.04210861, -0.020748941, -0.08971619, -0.041533835, 0.049955353, -0.001552015, -0.021463478, -0.021696063, -0.07944883, 0.06588757, -0.03423181, 0.012767491, -0.033467237, -0.043991882, -0.04137954, -0.012640813, -0.015641512, 0.005836557, -0.055145193, 0.07181472, -0.06706709, 0.02758981, 0.012491536, 1.7908428E-4, 0.04731288, -0.068052836, -0.0071785594, -0.010232609, -5.460614E-34, 0.02516568, 0.034118056, -0.024733437, 0.047228355, 0.0037465394, -0.070258, 0.006290882, 0.15288313, -0.036288474, 0.040884007, 0.037519526, -0.06638392, -0.10930901, -0.05393522, 0.051463563, 0.01380731, 0.092907034, 0.09467754, -0.09783999, 0.01644662, -0.061126027, -0.066909626, -0.066924036, -0.012761488, -0.011370772, 0.042607214, 0.07927983, -0.032156847, 0.0015848099, -0.10566981, -0.07634261, -0.028213428, 0.05288052, 0.011874017, 0.040782917, -0.024232225, 0.019622972, -0.009141563, -0.017976653, 0.0110636735, 0.06362411, 0.0073917555, -0.048477355, 0.027756449, -0.08377103, -0.087621905, -0.10184008, -0.039954655, -0.040234677, 0.062480062, -0.033642195, -0.0564311, 0.06224413, -0.076749064, -0.074774526, 0.013139622, 0.028267289, 0.008429792, -0.057460103, 0.03531389, -0.014488331, 0.017556855, -0.0651587, 0.017372401, 0.07632589, -0.023450913, -0.06445739, 0.051610786, -0.08962435, 0.044742335, 0.03069502, 0.037950527, -0.030822052, -0.08677492, -0.046731796, -0.0776271, 0.06568365, 0.028590394, -0.032895997, -0.045174953, -0.02931815, -0.05048297, -0.017910603, 0.06758366, 0.07641755, 0.007941325, -0.043727882, 0.02192161, 0.0031555342, 0.045066938, 0.016599359, 0.031952247, 0.06343076, 0.11882935, 0.027208652, -2.0098744E-8, -0.030052101, -0.020225998, 0.0279905, 0.03370748, 0.045368966, 0.044222686, -0.0042009526, 0.022090353, 0.005018363, 0.044784073, -0.005220454, 0.009343863, -0.08612542, -0.03041207, 0.0015026716, -0.07573834, -0.027690666, -0.012998181, -0.096883155, 0.009344862, -0.09863915, -0.012999212, -0.014732585, -0.023914909, -0.0010928006, 0.031345252, -0.010144734, 0.1443564, 0.050369326, -0.013374743, -0.02448535, 0.033876654, -0.05207029, -0.002537805, -0.03773417, 0.026459645, 0.039215047, -0.059335854, 0.03636168, 0.020787522, -0.05464286, 0.002337255, -0.0017656129, 0.045326453, 0.100353494, -0.06540476, -0.0011178906, -0.03074571, -0.058903407, -0.058317985, -0.022108076, -0.03130717, -0.07358733, 0.09797297, -0.027214048, -0.04498124, 0.052540313, 0.042964745, 0.0020706856, 0.07419735, 0.003985519, -0.0688295, -0.012315984, -0.06117761]
DSS821S, DataStax Gray Track Jacket, [-0.07082191, 0.067412384, 0.06783657, 0.028603345, 0.03828375, -0.037949555, 0.05794316, -0.003418509, -0.08990597, -0.009408942, -0.012201685, -0.043370552, 0.04093374, -0.038866296, -0.020300569, 0.025369972, 0.016402928, -0.014057669, 0.0038023284, -0.016225139, -0.052726798, -0.05528334, -0.060208827, -0.015197618, -0.09819485, 0.08513898, 7.66444E-4, 0.054203793, -0.03671, -0.050062023, -0.053456023, -0.055068593, 0.013893794, 0.09232062, -0.02926019, -0.11421958, 0.033829447, 0.04143306, -0.16357696, 0.111164406, -0.02939019, -0.029281506, -0.0535517, -0.020903034, 0.0058977064, -0.019795945, -0.02559324, -0.047165964, -0.0135571305, 0.106381156, -0.033792708, -0.034029335, 0.02641418, 0.051884465, 0.027800158, 0.033796597, 0.030605061, 0.0794917, -0.032727078, -0.05218821, 0.008066298, -0.016971262, -0.015393368, -0.034827244, 0.10385865, 0.055413797, -0.07498812, 0.0229459, 0.0152547425, -0.02138506, 0.08530597, -0.042407386, -0.0053713648, -0.0023126763, -0.032112353, 0.12011494, -0.017133633, 0.01567088, 0.063325614, -0.08818123, -0.04391273, 0.0072948546, -0.009736846, 0.025253298, 0.06912026, 0.07062999, -0.015103997, -0.0024095138, -0.057653394, -0.0034386674, 0.009427716, 0.067399286, -0.062590875, 0.04188215, -0.03420959, 0.019589514, -0.053489, 0.052838285, 0.013057854, -0.00275586, -5.6561205E-4, -0.040460624, -0.027296832, 0.07828912, -0.09300721, -0.10551076, 0.041448724, -0.0033315546, -0.033108037, -0.061363954, -0.015482516, 0.009820238, -0.061283533, 0.01978057, -0.029703388, -0.04237483, -0.09110335, 0.07157788, -0.016250413, -0.044077586, -0.004866515, -0.0056495112, -0.057703096, -0.0046912692, -0.025307935, -0.07232841, 0.030311925, 1.8689306E-33, 0.015912542, -0.037780497, -0.030665092, -0.02079233, 0.045621842, -0.037489977, -0.0659675, -0.09876963, -0.0766289, 0.06602595, -0.0068284366, 0.07291259, -0.060869955, 0.068781935, -0.0051675006, -0.046433404, 0.02631474, 0.05507785, -0.040889807, -0.0034959437, 0.02740723, 0.014073561, 0.01172013, -0.07333261, 0.10200683, 0.08095819, -0.031093951, -0.0068012914, 0.04102993, 0.027227229, -0.08211715, -0.0694451, 0.08286581, 0.053655226, -0.03130123, 0.022624379, -0.031268977, 0.056532364, 0.0025787856, 0.026024906, 0.023102542, 0.046363864, 0.053285275, 0.0073795663, -0.076093875, 0.053824604, 0.11766238, -0.033342022, -0.0031524948, -0.030549273, 0.009456215, -0.044903807, 0.024666399, -0.060669728, 0.002780408, -0.029092694, 0.049255144, 0.016162949, 0.021088757, -0.05235903, 0.028282253, 0.05639632, 0.04406316, -0.09029827, 0.09748959, 0.059281446, 0.038586795, -0.05398832, -0.028016694, -0.011419294, 0.0074267834, 0.061614722, 0.10407695, 0.04794085, 0.13665845, -0.048971422, -0.027561616, 0.01872975, -0.08155038, -0.021480639, -0.10222782, -0.07763032, -0.055903386, 0.032896943, 0.01806057, -0.011516305, 0.022761976, 0.07406894, -0.055564776, -0.026622783, 0.007890165, -0.009417001, -0.077691086, 6.6603615E-4, -0.033632252, -1.4328852E-33, 0.09430495, 0.026841197, 0.09336842, 0.065417334, 0.034854233, 0.07341413, 0.06390816, 0.05255521, 0.05267035, 0.07461021, 0.124083884, -0.02945829, -0.03828202, -0.0014954064, -0.00859513, 0.05803593, -0.031593602, 0.058386672, -0.006543109, -0.097111516, -0.022556635, -0.06721671, -0.02415679, 0.09086159, 0.026417617, -0.01596764, 0.084916785, 0.04407472, -0.049959596, -0.08572871, -0.055773936, 0.011344343, -0.036553934, -0.053063568, 0.035733998, 0.02126725, 0.09403653, 0.049557354, -0.02007768, -0.019715892, -0.071951546, 0.0011798595, 0.028193858, 0.03213848, -0.012429662, -0.027776776, 0.0036961243, 0.07608478, -0.029230673, 0.026017928, 0.067992635, -0.014775331, 0.101934694, 0.03873499, 0.031708047, 0.06414092, -0.05415389, 0.043145977, -0.05681142, 0.053663082, 0.044734977, -0.0012090437, -0.071044646, -0.015353165, -0.0059510726, 0.009402352, -0.017786914, -0.0636017, -0.06165282, 0.029500443, 0.03016053, -0.0058814175, 0.0046585714, 0.024535565, 0.033438034, -0.1199713, 0.026317542, 0.07799079, 0.05092104, 0.058379225, 0.024528226, -0.02094227, 0.06822855, -0.02085887, 0.117472224, 0.10383591, 0.0044738287, 0.058364093, 0.010026867, -0.059164036, -0.022551868, -0.0020642874, -0.049125127, 0.12409695, -0.07603761, -1.4415056E-8, -0.01032722, 0.0066188723, 0.023206534, -0.04794078, -0.037860442, -0.007744759, -0.0038590003, 0.019159187, 0.04409525, -0.041403227, 0.088419005, -0.022698922, -0.055370957, 0.036499146, -0.054483455, -0.043757446, -0.015926925, 0.044429805, 0.019716486, -0.02384877, -0.030869994, 0.0023680471, -0.01869198, 0.019960226, 0.018036019, 0.036074042, 0.029235808, 0.03162693, 0.060086507, -0.008958177, -0.013412854, -0.0022745554, 0.049675003, -0.043192577, 0.053736094, -0.053503603, -0.02994777, 0.07568316, 0.063537575, -0.026482819, -0.021258894, 0.0014044087, 0.01294437, -0.03405489, 0.021664422, -0.04247615, -0.002873527, -0.0132805295, -0.05026854, -0.017103516, 0.06887473, -0.043486964, -0.021892458, 0.046017338, 0.0072411373, -0.031530567, 0.0098563945, 0.04238664, -0.055596694, 0.03561711, -0.069966376, -0.10696296, -0.019438252, 0.04880644]
APC30L, Apache Cassandra 3.0 Contributor T-Shirt, [-0.017913612, 0.047000837, -0.043849207, 0.0320785, -0.0053036395, -0.021053873, -0.0510617, -0.036407106, -0.025608156, 0.03063186, 0.04003666, -0.112480514, 0.098846786, -0.033050206, -0.029417852, 0.008438278, 0.052184332, 0.0082579795, 0.026072733, -0.05666697, -0.14857872, 0.02331566, 0.08416891, 0.03449314, 0.022938794, -0.053468447, -0.07507965, 0.0015881484, 0.02584784, -0.011609371, -0.065646976, 0.034109406, -0.00873094, 0.04809617, -0.023239857, 0.028126223, 0.07264339, 0.063899845, -0.049096376, 7.085461E-4, 0.0671483, -0.13430321, -0.06458689, -0.012288966, -0.0434386, -0.033283003, -0.060309578, 0.055121243, -0.050286215, 5.233863E-4, 0.013903211, 0.007861445, 0.064051665, -0.05138158, -0.035405554, 0.015251613, 0.023035768, 0.030493988, 0.052688994, 0.0097718425, 0.060327645, -0.035902463, -0.066695884, 0.008154781, 0.06481256, -0.024584973, 0.043381378, -0.0059541496, -0.017688017, -0.0015079728, 0.033911046, -0.018174449, 0.0251702, 0.022316014, 0.06563447, 0.13551778, 0.034431376, -0.043241847, -0.032092266, 0.009341933, -0.040611338, 0.057520874, -5.0422136E-4, 0.049166363, -0.088640474, 0.0958228, -0.077705935, -0.043835163, -0.01593893, -0.06053097, 0.008450051, -4.2704228E-4, 0.06020406, -0.07424454, -0.10646737, 0.06178337, -0.019642547, 0.012083956, -0.028222624, 0.073623456, -0.08429736, -0.01571496, -0.033686068, 0.01196859, 0.0010389817, -0.044592083, -0.025530482, 0.013293521, 0.001544766, 0.0020151106, 0.04181134, -0.033286437, -0.10202224, -0.08017806, -0.030387813, 0.011046111, 0.03426501, -0.03168553, 0.009145825, 0.004248442, 0.04672902, -0.012934952, -0.048126597, -0.017077424, 0.056967825, -0.005555937, 0.029967856, -1.189356E-33, 0.047995888, 0.12019559, 0.07932185, 0.01561063, 0.09149555, -0.045048602, -0.008182393, -0.090856306, -0.06024976, -0.073559664, 0.045047697, 0.046530616, 0.033840552, 0.03950069, -0.04212517, 0.033299178, -0.030490927, -0.041392326, -0.053736217, -0.056381002, 0.029232897, -0.035194196, -0.01103066, 0.09038407, 0.020801729, 0.030104226, 0.060822263, -0.0038590173, 0.03238856, 0.014346756, 0.019102288, 0.04675445, 0.06818796, 0.00854537, -0.046038248, 0.005303503, -0.021207888, 0.008991518, -0.00824011, -0.02623915, 0.01236104, 0.06158607, 0.06662846, -0.039666433, -0.042848926, 0.007752915, 0.0959426, -0.021174036, 0.041021746, 0.04060229, 0.045320235, 0.0054344847, 0.046189968, 0.02076138, 0.010343238, -0.047209438, 0.05064839, 0.011074255, 0.041159682, -0.04405103, -0.032298513, -0.007062093, -0.005439647, 0.011709815, -5.498317E-4, 0.013430805, -0.07582177, -0.0044922726, 0.008728275, -0.036665566, 0.015555299, 0.10194091, 0.044371087, 0.025311204, -0.07731574, -0.01664033, -0.05510649, 0.015231506, -0.014826043, 0.049887642, 0.0037054021, -0.078957066, -0.03054639, -0.022782126, 0.008368401, -0.04503434, 0.0019858174, 0.013603871, 0.01314832, -0.031425796, 0.15306784, 0.083572656, 0.06433284, -0.018485565, -0.048573047, 2.801045E-34, 0.011235869, 0.0403196, 0.045947522, 0.03184005, 0.111179486, -0.072355874, -0.08857451, 0.058404718, -0.0024915547, 0.022987673, 0.056480512, -0.021095421, -0.056352947, -0.059324004, 0.003082116, 0.05586708, 0.0594541, 0.023976443, -0.080878615, -0.019191578, -0.0392988, -0.0018610231, -0.0040588803, -0.012522939, 0.040240742, -0.057695422, 0.07031197, 0.048392255, -0.06645199, -0.039659094, -0.06895391, -0.0062983898, -0.030642759, -0.005776513, 0.07274903, -0.037262015, -0.03957959, 0.06419157, 0.016195504, -0.010096385, 0.004285717, 0.007183841, 0.02113645, 0.043952297, -0.018750252, 0.01167804, 0.011729709, -0.06731694, -0.04926297, 9.39064E-4, 0.027929222, -0.06439326, 0.12858745, 0.051263515, 0.04353574, 0.085619375, 0.023755651, 0.1133155, 0.07134263, -0.0075644944, 0.034379575, -0.0016249892, -0.07492801, 0.016605027, 0.014762336, -0.013138342, -0.03272419, 0.030115588, -0.086654074, 0.025713153, -0.019028977, -0.042360537, -0.018025925, -0.06687901, 0.045015123, -0.09872604, -0.029978108, 0.07611114, -0.07221513, 0.002692615, -0.07357469, -0.008396086, -0.023592995, 0.027149083, 0.15226306, -0.004369929, -4.1260748E-4, 0.050630223, -0.040522877, 0.09083433, -0.046994194, 0.05209577, -0.054825496, 0.06677913, 0.09477359, -1.7028803E-8, 0.018177489, -0.06811902, -0.124672234, 0.010909696, 0.11497654, 0.062213942, 0.040133845, 0.0056362427, -0.011733884, 0.14600664, -0.014915122, -0.022864783, -0.021209562, -0.020202309, 0.0522734, -0.098391905, -0.0071428437, -0.019954266, -0.12774442, -0.10894838, -0.033263102, -0.0015002876, 0.045023546, 7.485474E-4, -0.01221141, 0.079038575, -0.03630546, 0.03672663, -0.011360921, -0.0509164, -0.077568986, -0.008009642, -0.046507247, -0.06849769, -0.036036983, 0.0369817, -0.031570267, 0.013020479, 0.03550005, 0.08041109, -0.03966381, 0.034658063, -0.035090398, 0.05666002, 0.014906023, -0.012224123, -0.05564539, 0.005969896, 0.00632337, -0.052299947, -0.018763155, -0.116111055, 0.042749047, -0.00213771, -0.042451177, -0.022335429, 0.04196325, 0.04572464, 0.09636175, 0.034945592, 0.0436888, -0.06595088, -0.03934413, 0.0022234828]
DSH916S, DataStax Black Hoodie, [-0.12901686, 0.06750878, -0.015875347, 0.048425958, 0.023996504, -0.061915256, 0.0843905, -0.014945756, -0.014037481, -0.018819511, 0.043719795, -0.042961694, 0.036557302, -0.073862106, 0.0043573575, -0.04561454, 0.021633076, -0.07767101, -0.016247192, -0.072705, -0.06822068, -0.09946159, -0.00767518, 0.035268124, -0.045257855, 0.04555528, 0.025004162, 0.041580714, -0.019663105, -0.054859936, -0.0035147779, -0.06167154, -0.00969919, 0.055340353, -0.0030772465, -0.094152, 0.069415554, 0.035156332, -0.10896679, 0.053886995, -0.050414868, -0.049542744, -0.08527266, -0.025659552, 0.0040562833, -0.05764964, 0.036245037, 0.030901907, 0.072715215, 0.032440886, -0.010414485, -0.05359395, -0.0041743573, 0.085962534, -0.05187989, -0.027256776, -2.2556375E-4, 0.06320389, 0.020836193, -0.04010338, 0.016916202, -0.05138942, -0.0053537586, 0.09301829, 0.07441338, 0.04121804, -0.049514707, -0.04344423, 0.024242407, -0.01885385, 0.0671296, 0.0030526626, -0.06736371, 0.047897045, -0.05036234, 0.062386334, 0.05945669, -0.044822905, 0.03993141, 0.06442393, -0.032335367, 0.023115125, 0.004612807, 0.10234248, 0.021567645, 0.030296266, -0.053878326, -0.0028513076, -0.056108326, -0.010724787, -0.003632716, 0.08597656, -0.047319014, 0.037577942, -0.062882334, -0.010735896, 0.010672188, -0.020657863, 0.0509316, 0.06911102, -0.0635718, -0.064823315, -0.0053034215, 0.0511878, -0.035146955, -0.057582412, -0.004953612, 0.021369375, 0.0073058517, -0.037574228, -0.08672969, 0.0203235, -0.06614526, 0.016954081, -0.018222578, -0.08218734, -0.04653076, 0.05529655, -0.0260986, -0.026508924, -0.032185216, -0.03560534, -0.08051421, -0.057192564, -0.017802441, -0.0493075, -0.0033284277, 1.6490092E-33, 0.01364493, -0.037281726, 0.040851798, -0.0023311034, 0.09764146, 0.0074244407, -0.008512869, -0.09636833, -0.09875595, 0.11985198, -0.014639988, 6.012371E-4, -0.10884095, 0.072424956, 0.08840018, -0.052623007, 0.030744808, -7.107857E-4, -0.032611724, -0.06867129, 0.009609768, 0.023441015, 0.024298092, -0.004840248, 0.0397257, 0.06170588, -0.029062677, 0.03018478, 0.06392695, 0.04425841, -0.11554484, -0.055407558, 0.07147228, 8.713611E-4, -0.040447067, -0.0032882378, -0.07129458, -0.048676822, 0.011611432, 0.0341814, 0.05635074, 0.04412518, 0.008132437, 0.009064346, -0.066895254, 0.07329042, 0.06798078, 0.0018936533, 0.0046871835, -0.0321353, 0.049457826, -0.06918459, 0.0070256125, -0.006924069, -0.014515852, 0.052084684, 0.009411835, -0.04372213, 0.045856643, 0.0077833124, 0.059718966, 0.04382525, 0.0699126, -0.045913674, 0.044959225, 0.008050179, 0.050918348, -0.021053098, -0.014731383, -0.023228781, -0.011979908, 0.11934541, 0.051671863, 0.034225777, 0.16783294, -0.028407106, -0.0013050596, 0.006338062, -0.022531306, -0.028635407, -0.02598476, -0.08916951, -0.016696902, 0.06711902, -0.04382255, 0.03799316, 0.0038380222, 0.060348693, 0.018686952, -0.008926359, -0.0361765, -0.05117616, -0.06190842, -0.0017070487, -0.05475645, -9.1600425E-34, 0.05793871, 0.0033936831, 0.06267004, 0.036977127, 0.08805148, 0.06141756, 0.06626246, 0.061615016, 0.02988189, 0.050998274, 0.13748293, 0.026111498, -0.06367024, 2.2110686E-5, 0.068628624, 0.10074156, 0.01977892, 0.016244436, -0.034209747, -0.061376534, -0.030804079, -0.013644809, -0.03158327, -0.03165341, -0.050665174, -0.03464297, -5.7415E-4, 0.11689936, -0.013466449, 0.00719917, -0.06467134, 0.016177464, -0.035081632, 0.053696398, 0.046807215, 0.032607853, 0.066758305, 0.029107098, 0.037173707, -0.0042550815, -0.0057522706, -0.03956576, -0.008362471, 0.07274572, -0.026587691, -0.043541837, 5.601993E-4, 0.015051743, 0.044065982, 3.575634E-4, -0.018251838, -0.016219137, 0.09369816, 0.16569701, 0.018938972, 0.006157212, 0.014289091, 0.023240263, -0.034351535, 0.03284955, 0.051928077, 0.013595051, -0.08631928, 0.0058084675, 0.006538688, -0.032973327, 0.011588472, -0.074198335, -0.061044406, 0.031628344, 0.076983206, -0.06027979, 0.022057429, 0.035741113, 0.016628403, -0.10440908, -0.0515884, 0.06771437, 0.028857483, 0.057743903, 0.017734189, -0.019641, 0.026703099, 0.030355213, 0.11861476, 0.05102727, 0.023570614, 0.08391981, 0.04379299, -0.029552389, -0.050897487, 0.022737397, -0.031663164, 0.059622236, 0.012532022, -1.4840581E-8, 0.025565444, -0.007569453, 0.07266404, -0.014461958, 0.022746854, -0.026543492, -0.07453234, -0.056099866, 0.053679176, -0.013680508, 0.07314722, 0.025112633, -0.0034581712, -0.05869054, -0.15318614, -0.009548202, -0.006189307, 0.016363312, 0.0640959, -0.06689665, -0.010971905, 0.033545714, 0.031447347, -0.061414696, 0.039394714, 0.031430554, -0.027277524, 0.054884586, 0.008618847, 0.021983465, 0.0077999947, -0.007172727, 0.050386876, -0.09795014, 0.048781306, -0.050041717, -0.056402046, 0.03111033, 0.022661677, -0.07249894, 0.048743863, -0.078595094, 0.016557528, -0.039893962, -0.030897513, 0.034660544, -0.012456049, 0.012119897, -0.034626145, 0.038878582, 0.048413444, -0.06584545, -0.056738283, 0.054527823, -0.040140975, -0.102604374, -5.8104744E-4, 0.04244653, -0.064685315, 0.019036675, -0.04618626, -0.071555994, -0.025133785, -0.023957023]
DSH916L, DataStax Black Hoodie, [-0.12901686, 0.06750878, -0.015875347, 0.048425958, 0.023996504, -0.061915256, 0.0843905, -0.014945756, -0.014037481, -0.018819511, 0.043719795, -0.042961694, 0.036557302, -0.073862106, 0.0043573575, -0.04561454, 0.021633076, -0.07767101, -0.016247192, -0.072705, -0.06822068, -0.09946159, -0.00767518, 0.035268124, -0.045257855, 0.04555528, 0.025004162, 0.041580714, -0.019663105, -0.054859936, -0.0035147779, -0.06167154, -0.00969919, 0.055340353, -0.0030772465, -0.094152, 0.069415554, 0.035156332, -0.10896679, 0.053886995, -0.050414868, -0.049542744, -0.08527266, -0.025659552, 0.0040562833, -0.05764964, 0.036245037, 0.030901907, 0.072715215, 0.032440886, -0.010414485, -0.05359395, -0.0041743573, 0.085962534, -0.05187989, -0.027256776, -2.2556375E-4, 0.06320389, 0.020836193, -0.04010338, 0.016916202, -0.05138942, -0.0053537586, 0.09301829, 0.07441338, 0.04121804, -0.049514707, -0.04344423, 0.024242407, -0.01885385, 0.0671296, 0.0030526626, -0.06736371, 0.047897045, -0.05036234, 0.062386334, 0.05945669, -0.044822905, 0.03993141, 0.06442393, -0.032335367, 0.023115125, 0.004612807, 0.10234248, 0.021567645, 0.030296266, -0.053878326, -0.0028513076, -0.056108326, -0.010724787, -0.003632716, 0.08597656, -0.047319014, 0.037577942, -0.062882334, -0.010735896, 0.010672188, -0.020657863, 0.0509316, 0.06911102, -0.0635718, -0.064823315, -0.0053034215, 0.0511878, -0.035146955, -0.057582412, -0.004953612, 0.021369375, 0.0073058517, -0.037574228, -0.08672969, 0.0203235, -0.06614526, 0.016954081, -0.018222578, -0.08218734, -0.04653076, 0.05529655, -0.0260986, -0.026508924, -0.032185216, -0.03560534, -0.08051421, -0.057192564, -0.017802441, -0.0493075, -0.0033284277, 1.6490092E-33, 0.01364493, -0.037281726, 0.040851798, -0.0023311034, 0.09764146, 0.0074244407, -0.008512869, -0.09636833, -0.09875595, 0.11985198, -0.014639988, 6.012371E-4, -0.10884095, 0.072424956, 0.08840018, -0.052623007, 0.030744808, -7.107857E-4, -0.032611724, -0.06867129, 0.009609768, 0.023441015, 0.024298092, -0.004840248, 0.0397257, 0.06170588, -0.029062677, 0.03018478, 0.06392695, 0.04425841, -0.11554484, -0.055407558, 0.07147228, 8.713611E-4, -0.040447067, -0.0032882378, -0.07129458, -0.048676822, 0.011611432, 0.0341814, 0.05635074, 0.04412518, 0.008132437, 0.009064346, -0.066895254, 0.07329042, 0.06798078, 0.0018936533, 0.0046871835, -0.0321353, 0.049457826, -0.06918459, 0.0070256125, -0.006924069, -0.014515852, 0.052084684, 0.009411835, -0.04372213, 0.045856643, 0.0077833124, 0.059718966, 0.04382525, 0.0699126, -0.045913674, 0.044959225, 0.008050179, 0.050918348, -0.021053098, -0.014731383, -0.023228781, -0.011979908, 0.11934541, 0.051671863, 0.034225777, 0.16783294, -0.028407106, -0.0013050596, 0.006338062, -0.022531306, -0.028635407, -0.02598476, -0.08916951, -0.016696902, 0.06711902, -0.04382255, 0.03799316, 0.0038380222, 0.060348693, 0.018686952, -0.008926359, -0.0361765, -0.05117616, -0.06190842, -0.0017070487, -0.05475645, -9.1600425E-34, 0.05793871, 0.0033936831, 0.06267004, 0.036977127, 0.08805148, 0.06141756, 0.06626246, 0.061615016, 0.02988189, 0.050998274, 0.13748293, 0.026111498, -0.06367024, 2.2110686E-5, 0.068628624, 0.10074156, 0.01977892, 0.016244436, -0.034209747, -0.061376534, -0.030804079, -0.013644809, -0.03158327, -0.03165341, -0.050665174, -0.03464297, -5.7415E-4, 0.11689936, -0.013466449, 0.00719917, -0.06467134, 0.016177464, -0.035081632, 0.053696398, 0.046807215, 0.032607853, 0.066758305, 0.029107098, 0.037173707, -0.0042550815, -0.0057522706, -0.03956576, -0.008362471, 0.07274572, -0.026587691, -0.043541837, 5.601993E-4, 0.015051743, 0.044065982, 3.575634E-4, -0.018251838, -0.016219137, 0.09369816, 0.16569701, 0.018938972, 0.006157212, 0.014289091, 0.023240263, -0.034351535, 0.03284955, 0.051928077, 0.013595051, -0.08631928, 0.0058084675, 0.006538688, -0.032973327, 0.011588472, -0.074198335, -0.061044406, 0.031628344, 0.076983206, -0.06027979, 0.022057429, 0.035741113, 0.016628403, -0.10440908, -0.0515884, 0.06771437, 0.028857483, 0.057743903, 0.017734189, -0.019641, 0.026703099, 0.030355213, 0.11861476, 0.05102727, 0.023570614, 0.08391981, 0.04379299, -0.029552389, -0.050897487, 0.022737397, -0.031663164, 0.059622236, 0.012532022, -1.4840581E-8, 0.025565444, -0.007569453, 0.07266404, -0.014461958, 0.022746854, -0.026543492, -0.07453234, -0.056099866, 0.053679176, -0.013680508, 0.07314722, 0.025112633, -0.0034581712, -0.05869054, -0.15318614, -0.009548202, -0.006189307, 0.016363312, 0.0640959, -0.06689665, -0.010971905, 0.033545714, 0.031447347, -0.061414696, 0.039394714, 0.031430554, -0.027277524, 0.054884586, 0.008618847, 0.021983465, 0.0077999947, -0.007172727, 0.050386876, -0.09795014, 0.048781306, -0.050041717, -0.056402046, 0.03111033, 0.022661677, -0.07249894, 0.048743863, -0.078595094, 0.016557528, -0.039893962, -0.030897513, 0.034660544, -0.012456049, 0.012119897, -0.034626145, 0.038878582, 0.048413444, -0.06584545, -0.056738283, 0.054527823, -0.040140975, -0.102604374, -5.8104744E-4, 0.04244653, -0.064685315, 0.019036675, -0.04618626, -0.071555994, -0.025133785, -0.023957023]
```
