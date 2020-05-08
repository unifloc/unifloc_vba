H_CORRELATION = 0 # 0 - BeggsBrill, 1 - Ansari and so on 
PVT_CORRELATION = 0 # 0 -Standing, 1 -McCain, 2 - linear 
PVT_DEFAULT = "gamma_gas:0,900;gamma_oil:0,750;gamma_wat:1,000;rsb_m3m3:100,000;rp_m3m3:-1,000;pb_atma:-1,000;tres_C:90,000;bob_m3m3:-1,000;muob_cP:-1,000;PVTcorr:0;ksep_fr:0,000;pksep_atma:-1,000;tksep_C:-1,000; " 
ESP_DEFAULT = "ESP_ID:1006.00000;HeadNom_m:2000.00000;ESPfreq_Hz:50.00000;ESP_U_V:1000.00000;MotorPowerNom_kW:30.00000;Tintake_C:85.00000;t_dis_C:25.00000;KsepGS_fr:0.00000;ESP_energy_fact_Whday:0.00000;ESP_cable_type:0;ESP_Hmes_m:0.00000;ESP_gas_degradation_type:0;c_calibr_head:0.00000;PKV_work_min:-1,00000;PKV_stop_min:-1,00000;"
WELL_DEFAULT = "hperf_m:2000,00000;hpump_m:1800,00000;udl_m:0,00000;d_cas_mm:150,00000;dtub_mm:72,00000;dchoke_mm:15,00000;roughness_m:0,00010;tbh_C:85,00000;twh_C:25,00000;"
WELL_GL_DEFAULT = "hperf_m:2500,00000;htub_m:2000,00000;udl_m:0,00000;d_cas_mm:125,00000;dtub_mm:62,00000;dchoke_mm:15,00000;roughness_m:0,00010;tbh_C:100,00000;twh_C:50,00000;GLV:1;H_glv_m:1500,000;d_glv_mm:5,000;p_glv_atma:50,000;"
const_gg_ = 0.6 
const_gw_ = 1 
const_go_ = 0.86 
const_sigma_wat_gas_Nm = 0.01 
const_sigma_oil_Nm = 0.025 
const_mu_w = 0.36
const_mu_g = 0.0122 
const_mu_o = 0.7 
const_rsb_default = 100 
const_Bob_default = 1.2 
const_tres_default = 90 
const_Roughness_default = 0.0001 
StartEndTemp = 0 
Standing_based = 0 
const_rho_air = 1.2217 
 
import xlwings as xw
addin_name_str = "UniflocVBA_7.xlam"
class API():
    def __init__(self, addin_name_str):
        self.book = xw.Book(addin_name_str)
    def MF_CJT_Katm(self, p_atma,t_C,str_PVT=PVT_DEFAULT,qliq_sm3day=10,fw_perc=0):
        """
 ========== description ============== 
 функция расчета коэффициента Джоуля Томсона 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     str_pvt - encoded to string pvt properties of fluid    

     qliq_sm3day - liquid rate (at surface)    

     fw_perc - water fraction (watercut)  output - number   

        """

        self.f_MF_CJT_Katm = self.book.macro("MF_CJT_Katm")
        return self.f_MF_CJT_Katm(p_atma,t_C,str_PVT,qliq_sm3day,fw_perc)

    def MF_q_mix_rc_m3day(self, qliq_sm3day,fw_perc,p_atma,t_C,str_PVT=PVT_DEFAULT):
        """
 ========== description ============== 
 расчет объемного расхода газожидкостной смеси  для заданных термобарических условий 
        
 ==========  arguments  ============== 

     qliq_sm3day- дебит жидкости на поверхности    

     fw_perc - объемная обводненность    

     p_atma - давление, атм    

     t_c - температура, с.    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_MF_q_mix_rc_m3day = self.book.macro("MF_q_mix_rc_m3day")
        return self.f_MF_q_mix_rc_m3day(qliq_sm3day,fw_perc,p_atma,t_C,str_PVT)

    def MF_rho_mix_kgm3(self, qliq_sm3day,fw_perc,p_atma,t_C,str_PVT=PVT_DEFAULT):
        """
 ========== description ============== 
 расчет плотности газожидкостной смеси для заданных условий 
        
 ==========  arguments  ============== 

     qliq_sm3day- дебит жидкости на поверхности    

     fw_perc - объемная обводненность    

     p_atma - давление, атм    

     t_c - температура, с.    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_MF_rho_mix_kgm3 = self.book.macro("MF_rho_mix_kgm3")
        return self.f_MF_rho_mix_kgm3(qliq_sm3day,fw_perc,p_atma,t_C,str_PVT)

    def MF_mu_mix_cP(self, qliq_sm3day,fw_perc,p_atma,t_C,str_PVT=PVT_DEFAULT):
        """
 ========== description ============== 
 расчет вязкости газожидкостной смеси  для заданных термобарических условий 
        
 ==========  arguments  ============== 

     qliq_sm3day - дебит жидкости на поверхности    

     fw_perc - объемная обводненность    

     p_atma - давление, атм    

     t_c - температура, с.    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_MF_mu_mix_cP = self.book.macro("MF_mu_mix_cP")
        return self.f_MF_mu_mix_cP(qliq_sm3day,fw_perc,p_atma,t_C,str_PVT)

    def MF_gas_fraction_d(self, p_atma,t_C,fw_perc=0,str_PVT=PVT_DEFAULT,ksep_add_fr=0):
        """
 ========== description ============== 
 расчет доли газа в потоке 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     fw_perc - обводненность объемная    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения    

     ksep_add_fr - коэффициент сепарации дополнительный  для сепарации заданной в потоке. применяется  для сепарации при искомом давлении   

        """

        self.f_MF_gas_fraction_d = self.book.macro("MF_gas_fraction_d")
        return self.f_MF_gas_fraction_d(p_atma,t_C,fw_perc,str_PVT,ksep_add_fr)

    def MF_p_gas_fraction_atma(self, free_gas_d,t_C,fw_perc,str_PVT=PVT_DEFAULT,ksep_add_fr=0):
        """
 ========== description ============== 
 расчет давления при котором  достигается заданная доля газа в потоке 
        
 ==========  arguments  ============== 

     free_gas_d - допустимая доля газа в потоке;    

     t_c - температура, с;    

     fw_perc - объемная обводненность, проценты %;    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения.    

     ksep_add_fr - коэффициент сепарации дополнительный  для сепарации заданной в потоке. применяется  для сепарации при искомом давлении   

        """

        self.f_MF_p_gas_fraction_atma = self.book.macro("MF_p_gas_fraction_atma")
        return self.f_MF_p_gas_fraction_atma(free_gas_d,t_C,fw_perc,str_PVT,ksep_add_fr)

    def MF_rp_gas_fraction_m3m3(self, free_gas_d,p_atma,t_C,fw_perc,str_PVT=PVT_DEFAULT,Rp_limit_m3m3=500,ksep_add_fr=0):
        """
 ========== description ============== 
 расчет газового фактора  при котором достигается заданная доля газа в потоке 
        
 ==========  arguments  ============== 

     free_gas_d - допустимая доля газа в потоке    

     p_atma - давление, атм    

     t_c - температура, с.    

     fw_perc - объемная обводненность, проценты %;    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения    

     rp_limit_m3m3 - верхняя граница оценки гф    

     ksep_add_fr - коэффициент сепарации дополнительный  для сепарации заданной в потоке. применяется  для сепарации при искомом давлении   

        """

        self.f_MF_rp_gas_fraction_m3m3 = self.book.macro("MF_rp_gas_fraction_m3m3")
        return self.f_MF_rp_gas_fraction_m3m3(free_gas_d,p_atma,t_C,fw_perc,str_PVT,Rp_limit_m3m3,ksep_add_fr)

    def MF_ksep_natural_d(self, qliq_sm3day,fw_perc,p_intake_atma,t_intake_C=50,d_intake_mm=90,d_cas_mm=120,str_PVT=PVT_DEFAULT):
        """
 ========== description ============== 
 расчет натуральной сепарации газа на приеме насоса 
        
 ==========  arguments  ============== 

     qliq_sm3day - дебит жидкости в поверхностных условиях    

     fw_perc - обводненность    

     p_intake_atma - давление сепарации    

     t_intake_c - температура сепарации    

     d_intake_mm - диаметр приемной сетки    

     d_cas_mm - диаметр эксплуатационной колонны    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_MF_ksep_natural_d = self.book.macro("MF_ksep_natural_d")
        return self.f_MF_ksep_natural_d(qliq_sm3day,fw_perc,p_intake_atma,t_intake_C,d_intake_mm,d_cas_mm,str_PVT)

    def MF_ksep_total_d(self, SepNat,SepGasSep):
        """
 ========== description ============== 
 расчет общей сепарации на приеме насоса 
        
 ==========  arguments  ============== 

     sepnat - естественная сепарация    

     sepgassep - искусственная сепарация (газосепаратор)  mf_ksep_total_d = sepnat + (1 - sepnat) * sepgassep end function   

        """

        self.f_MF_ksep_total_d = self.book.macro("MF_ksep_total_d")
        return self.f_MF_ksep_total_d(SepNat,SepGasSep)

    def MF_dpdl_atmm(self, d_m,p_atma,Ql_rc_m3day,Qg_rc_m3day,mu_oil_cP=const_mu_o,mu_gas_cP=const_mu_g,sigma_oil_gas_Nm=const_sigma_oil_Nm,rho_lrc_kgm3=const_go_*1000,rho_grc_kgm3=const_gg_*const_rho_air,eps_m=0.0001,theta_deg=90,hcorr=1,param_out=0,c_calibr_grav=1,c_calibr_fric=1):
        """
 ========== description ============== 
расчет градиента давления с использованием многофазных корреляций 
        
 ==========  arguments  ============== 

     d_m - диаметр трубы в которой идет поток    

     p_atma - давление в точке расчета    

     ql_rc_m3day - дебит жидкости в рабочих условиях    

     qg_rc_m3day - дебит газа в рабочих условиях    

     mu_oil_cp - вязкость нефти в рабочих условиях    

     mu_gas_cp - вязкость газа в рабочих условиях    

     sigma_oil_gas_nm - поверхностное натяжение  жидкость газ    

     rho_lrc_kgm3 - плотность нефти    

     rho_grc_kgm3 - плотность газа    

     eps_m - шероховатость    

     theta_deg - угол от горизонтали    

     hcorr - тип корреляции    

     param_out - параметр для вывода    

     c_calibr_grav - калибровка гравитации    

     c_calibr_fric - калибровка трения   

        """

        self.f_MF_dpdl_atmm = self.book.macro("MF_dpdl_atmm")
        return self.f_MF_dpdl_atmm(d_m,p_atma,Ql_rc_m3day,Qg_rc_m3day,mu_oil_cP,mu_gas_cP,sigma_oil_gas_Nm,rho_lrc_kgm3,rho_grc_kgm3,eps_m,theta_deg,hcorr,param_out,c_calibr_grav,c_calibr_fric)

    def MF_calibr_pipeline(self, p_calc_from_atma,p_calc_to_atma,t_calc_from_C,t_val,h_list_m,diam_list_mm,qliq_sm3day,fw_perc,q_gas_sm3day=0,str_PVT=PVT_DEFAULT,calc_flow_direction=11,hydr_corr=H_CORRELATION,temp_methodTEMP_CALC_METHOD=StartEndTemp,c_calibr=1,roughness_m=0.0001,out_curves=1,out_curves_num_points=20,calibr_type=0):
        """
 ========== description ============== 
 подбор параметров потока через трубу при известном  перепаде давления с использованием многофазных корреляций 
        
 ==========  arguments  ============== 

    p_calc_from_atma - давление начальное, атм  граничное значение для проведения расчета    

    p_calc_to_atma - давление конечное, атм  граничное значение для проведения расчета    

     t_calc_from_c - температура в точке где задано давление расчета    

     t_val - температура вдоль трубопровода  если число то температура на другом конце трубы  если range или таблица [0..n,0..1] то температура  окружающей среды по вертикальной гл..см.мануал   

     h_list_m - траектория трубопровода, если число то измеренная  длина, range или таблица [0..n,0..1] то траектория    

     diam_list_mm - внутрнний диаметр трубы, если число то задается  постоянный диаметр, если range или таблица [0..n,0..1]  то задается зависимость диаметра от измеренной длины    

     qliq_sm3day - дебит жидкости в поверхностных условиях, нм3/сут    

     fw_perc - обводненность объемная в стандартных условиях    

     если qliq_sm3day =0 и q_gas_sm3day > 0  тогда считается барботаж газа через жидкость  fw_perc - обводненность объемная в стандартных условиях  q_gas_sm3day - свободный газ нм3..см.мануал   

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения  если задан флаг gas_only = 1 то жидкость не учитывается    

     calc_flow_direction - направление расчета и потока относительно  координат. 11 расчет и поток по координате  10 расчет по коордиате, поток против  00 расчет и поток против коо..см.мануал   

     hydr_corr - гидравлическая корреляция, h_correlation  beggsbrill = 0,  ansari = 1,  unified = 2,  gray = 3,  hagedornbrown = 4,  sakharovmokhov = 5    

     temp_method - метод расчета температуры  0 - линейное распределение по длине  1 - температура равна температуре окружающей среды  2 - расчет температуры с учетом эмиссии в окр..см.мануал   

     c_calibr - поправка на гравитационную составляющую  перепада давления, если дать ссылку на две ячейки,  то вторая будет поправка на трение.    

     roughness_m - шероховатость трубы    

     out_curves - флаг вывод значений между концами трубы  1 основные, 2 все значения.  вывод может замедлять расчет (не сильно)    

     out_curves_num_points - количество точек для вывода значений  между концами трубы.    

     calibr_type - тип калибровки  0 - подбор параметра c_calibr_grav  1 - подбор параметра c_calibr_fric  2 - подбор газового фактор  3 - подбор обводненности   

        """

        self.f_MF_calibr_pipeline = self.book.macro("MF_calibr_pipeline")
        return self.f_MF_calibr_pipeline(p_calc_from_atma,p_calc_to_atma,t_calc_from_C,t_val,h_list_m,diam_list_mm,qliq_sm3day,fw_perc,q_gas_sm3day,str_PVT,calc_flow_direction,hydr_corr,temp_method,c_calibr,roughness_m,out_curves,out_curves_num_points,calibr_type)

    def MF_calibr_pipe(self, p_calc_from_atma,p_calc_to_atma,t_calc_from_C,t_calc_to_C,length_m,theta_deg,d_mm,qliq_sm3day,fw_perc,q_gas_sm3day=0,str_PVT=PVT_DEFAULT,calc_flow_direction=11,hydr_corr=H_CORRELATION,c_calibr=1,roughness_m=0.0001,calibr_type=0):
        """
 ========== description ============== 
 подбор параметров потока через трубу при известном  перепаде давления с использованием многофазных корреляций 
        
 ==========  arguments  ============== 

    p_calc_from_atma - давление с которого начинается расчет, атм  граничное значение для проведения расчета    

   p_calc_to_atma   

     t_calc_from_c - температура в точке где задано давление, с    

     t_calc_to_c - температура на другом конце трубы  по умолчанию температура вдоль трубы постоянна  если задано то меняется линейно по трубе    

     length_m - длина трубы, измеренная, м    

     theta_deg - угол направления потока к горизонтали    

     d_mm - внутренний диаметр трубы    

     qliq_sm3day - дебит жидкости в поверхностных условиях    

     fw_perc - обводненность    

     если qliq_sm3day =0 и q_gas_sm3day > 0  тогда считается барботаж газа через жидкость  fw_perc - обводненность  q_gas_sm3day - свободный газ. дополнительный к pvt потоку.    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения  если задан флаг gas_only = 1 то жидкость не учитывается    

     calc_flow_direction - направление расчета и потока  относительно координат  если = 11 расчет и поток по координате  если = 10 расчет по, поток против координат  если = 00 рас..см.мануал   

     hydr_corr - гидравлическая корреляция, h_correlation  beggsbrill = 0  ansari = 1  unified = 2  gray = 3  hagedornbrown = 4  sakharovmokhov = 5    

     c_calibr - поправка на гравитационную составляющую  перепада давления, если дать ссылку на две ячейки,  то вторая будет поправка на трение    

     roughness_m - шероховатость трубы  out_curves - флаг вывод значений между концами трубы  0 минимум, 1 основные, 2 все значения.  вывод может замедлять расчет (не сильно)  out..см.мануал   

   calibr_type  

        """

        self.f_MF_calibr_pipe = self.book.macro("MF_calibr_pipe")
        return self.f_MF_calibr_pipe(p_calc_from_atma,p_calc_to_atma,t_calc_from_C,t_calc_to_C,length_m,theta_deg,d_mm,qliq_sm3day,fw_perc,q_gas_sm3day,str_PVT,calc_flow_direction,hydr_corr,c_calibr,roughness_m,calibr_type)

    def MF_calibr_choke(self, qliq_sm3day,fw_perc,d_choke_mm,p_in_atma=-1,p_out_atma=-1,d_pipe_mm=70,t_choke_C=20,str_PVT=PVT_DEFAULT,q_gas_sm3day=0,calibr_type=0):
        """
 ========== description ============== 
 расчет корректирующего фактора (множителя) модели штуцера под замеры  медленный расчет - калибровка подбирается 
        
 ==========  arguments  ============== 

     qliq_sm3day - дебит жидкости в ст. условиях    

     fw_perc - обводненность    

     d_choke_mm - диаметр штуцера (эффективный), мм    

     p_in_atma - давление на входе (высокой стороне)    

     p_out_atma - давление на выходе (низкой стороне)    

     d_pipe_mm - диаметр трубы до и после штуцера, мм    

     t_choke_c - температура, с.    

     str_pvt - закодированная строка с параметрами pvt,  если задана - перекрывает другие значения    

     q_gas_sm3day - свободный газ. дополнительный к pvt потоку.    

     calibr_type - тип калибровки  0 - подбор параметра c_calibr  1 - подбор диаметра штуцера  2 - подбор газового фактор  3 - подбор обводненности  4 - подбор дебита жидкости  ..см.мануал  

        """

        self.f_MF_calibr_choke = self.book.macro("MF_calibr_choke")
        return self.f_MF_calibr_choke(qliq_sm3day,fw_perc,d_choke_mm,p_in_atma,p_out_atma,d_pipe_mm,t_choke_C,str_PVT,q_gas_sm3day,calibr_type)

    def MF_p_pipeline_atma(self, p_calc_from_atma,t_calc_from_C,t_val,h_list_m,diam_list_mm,qliq_sm3day,fw_perc,q_gas_sm3day=0,str_PVT=PVT_DEFAULT,calc_flow_direction=11,hydr_corr=H_CORRELATION,temp_methodTEMP_CALC_METHOD=StartEndTemp,c_calibr=1,roughness_m=0.0001,out_curves=1,out_curves_num_points=20,num_value=0):
        """
 ========== description ============== 
 расчет распределения давления и температуры в трубопроводе  с использованием многофазных корреляций 
        
 ==========  arguments  ============== 

     p_calc_from_atma - давление с которого начинается расчет, атм  граничное значение для проведения расчета    

     t_calc_from_c - температура в точке где задано давление расчета    

     t_val - температура вдоль трубопровода  если число то температура на другом конце трубы  если range или таблица [0..n,0..1] то температура  окружающей среды по вертикальной гл..см.мануал   

     h_list_m - траектория трубопровода, если число то измеренная  длина, range или таблица [0..n,0..1] то траектория    

     diam_list_mm - внутрнний диаметр трубы, если число то задается  постоянный диаметр, если range или таблица [0..n,0..1]  то задается зависимость диаметра от измеренной длины    

     qliq_sm3day - дебит жидкости в поверхностных условиях, нм3/сут    

     fw_perc - обводненность объемная в стандартных условиях    

     если qliq_sm3day =0 и q_gas_sm3day > 0  тогда считается барботаж газа через жидкость  fw_perc - обводненность объемная в стандартных условиях  q_gas_sm3day - свободный газ нм3..см.мануал   

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения  если задан флаг gas_only = 1 то жидкость не учитывается    

     calc_flow_direction - направление расчета и потока относительно  координат. 11 расчет и поток по координате  10 расчет по коордиате, поток против  00 расчет и поток против коо..см.мануал   

     hydr_corr - гидравлическая корреляция, h_correlation  beggsbrill = 0,  ansari = 1,  unified = 2,  gray = 3,  hagedornbrown = 4,  sakharovmokhov = 5    

     temp_method - метод расчета температуры  0 - линейное распределение по длине  1 - температура равна температуре окружающей среды  2 - расчет температуры с учетом эмиссии в окр..см.мануал   

     c_calibr - поправка на гравитационную составляющую  перепада давления, если дать ссылку на две ячейки,  то вторая будет поправка на трение.    

     roughness_m - шероховатость трубы    

     out_curves - флаг вывод значений между концами трубы  1 основные, 2 все значения.  вывод может замедлять расчет (не сильно)    

     out_curves_num_points - количество точек для вывода значений  между концами трубы.    

     num_value - значение которое будет выводиться первым   

        """

        self.f_MF_p_pipeline_atma = self.book.macro("MF_p_pipeline_atma")
        return self.f_MF_p_pipeline_atma(p_calc_from_atma,t_calc_from_C,t_val,h_list_m,diam_list_mm,qliq_sm3day,fw_perc,q_gas_sm3day,str_PVT,calc_flow_direction,hydr_corr,temp_method,c_calibr,roughness_m,out_curves,out_curves_num_points,num_value)

    def MF_p_pipe_atma(self, p_calc_from_atma,t_calc_from_C,t_calc_to_C,length_m,theta_deg,d_mm,qliq_sm3day,fw_perc,q_gas_sm3day=0,str_PVT=PVT_DEFAULT,calc_flow_direction=11,hydr_corr=H_CORRELATION,c_calibr=1,roughness_m=0.0001,out_curves=1,out_curves_num_points=20,num_value=0):
        """
 ========== description ============== 
 расчет распределения давления и температуры в трубе  с использованием многофазных корреляций 
        
 ==========  arguments  ============== 

    p_calc_from_atma - давление с которого начинается расчет, атм  граничное значение для проведения расчета    

     t_calc_from_c - температура в точке где задано давление, с    

     t_calc_to_c - температура на другом конце трубы  по умолчанию температура вдоль трубы постоянна  если задано то меняется линейно по трубе    

     length_m - длина трубы, измеренная, м    

     theta_deg - угол направления потока к горизонтали    

     d_mm - внутренний диаметр трубы    

     qliq_sm3day - дебит жидкости в поверхностных условиях    

     fw_perc - обводненность    

     если qliq_sm3day =0 и q_gas_sm3day > 0  тогда считается барботаж газа через жидкость  fw_perc - обводненность  q_gas_sm3day - свободный газ. дополнительный к pvt потоку.    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения  если задан флаг gas_only = 1 то жидкость не учитывается    

     calc_flow_direction - направление расчета и потока  относительно координат  если = 11 расчет и поток по координате  если = 10 расчет по, поток против координат  если = 00 рас..см.мануал   

     hydr_corr - гидравлическая корреляция, h_correlation  beggsbrill = 0  ansari = 1  unified = 2  gray = 3  hagedornbrown = 4  sakharovmokhov = 5    

     c_calibr - поправка на гравитационную составляющую  перепада давления, если дать ссылку на две ячейки,  то вторая будет поправка на трение    

     roughness_m - шероховатость трубы    

     out_curves - флаг вывод значений между концами трубы  0 минимум, 1 основные, 2 все значения.  вывод может замедлять расчет (не сильно)    

     out_curves_num_points - количество точек для вывода значений  между концами трубы.    

     num_value - значение которое будет выводиться первым   

        """

        self.f_MF_p_pipe_atma = self.book.macro("MF_p_pipe_atma")
        return self.f_MF_p_pipe_atma(p_calc_from_atma,t_calc_from_C,t_calc_to_C,length_m,theta_deg,d_mm,qliq_sm3day,fw_perc,q_gas_sm3day,str_PVT,calc_flow_direction,hydr_corr,c_calibr,roughness_m,out_curves,out_curves_num_points,num_value)

    def MF_p_choke_atma(self, qliq_sm3day,fw_perc,d_choke_mm,p_calc_from_atma=-1,calc_along_flow=True,d_pipe_mm=70,t_choke_C=20,c_calibr_fr=1,str_PVT=PVT_DEFAULT,q_gas_sm3day=0):
        """
 ========== description ============== 
 расчет давления в штуцере 
        
 ==========  arguments  ============== 

     qliq_sm3day - дебит жидкости в поверхностных условиях    

     fw_perc - обводненность    

     d_choke_mm - диаметр штуцера (эффективный)    

     p_calc_from_atma - давление с которого начинается расчет, атм  граничное значение для проведения расчета  либо давление на входе, либое на выходе    

     calc_along_flow - флаг направления расчета относительно потока  если = 1 то расчет по потоку  ищется давление на выкиде по известному давлению на входе,  ищется линейное давле..см.мануал   

     d_pipe_mm - диаметр трубы до и после штуцера    

     t_choke_c - температура, с.    

     c_calibr_fr - поправочный коэффициент на штуцер  1 - отсутсвие поправки  q_choke_real = c_calibr_fr * q_choke_model    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения    

     q_gas_sm3day - свободный газ. дополнительный к pvt потоку.   

        """

        self.f_MF_p_choke_atma = self.book.macro("MF_p_choke_atma")
        return self.f_MF_p_choke_atma(qliq_sm3day,fw_perc,d_choke_mm,p_calc_from_atma,calc_along_flow,d_pipe_mm,t_choke_C,c_calibr_fr,str_PVT,q_gas_sm3day)

    def MF_calibr_choke_fast(self, qliq_sm3day,fw_perc,d_choke_mm,p_in_atma=-1,p_out_atma=-1,d_pipe_mm=70,t_choke_C=20,str_PVT=PVT_DEFAULT,q_gas_sm3day=0):
        """
 ========== description ============== 
 расчет корректирующего фактора (множителя) модели штуцера под замеры  быстрый расчет - калибровка вычисляется 
        
 ==========  arguments  ============== 

     qliq_sm3day - дебит жидкости в ст. условиях    

     fw_perc - обводненность    

     d_choke_mm - диаметр штуцера (эффективный), мм    

     p_in_atma - давление на входе (высокой стороне)    

     p_out_atma - давление на выходе (низкой стороне)    

     d_pipe_mm - диаметр трубы до и после штуцера, мм    

     t_choke_c - температура, с.    

     str_pvt - закодированная строка с параметрами pvt,  если задана - перекрывает другие значения    

     q_gas_sm3day - свободный газ. дополнительный к pvt потоку.   

        """

        self.f_MF_calibr_choke_fast = self.book.macro("MF_calibr_choke_fast")
        return self.f_MF_calibr_choke_fast(qliq_sm3day,fw_perc,d_choke_mm,p_in_atma,p_out_atma,d_pipe_mm,t_choke_C,str_PVT,q_gas_sm3day)

    def MF_q_choke_sm3day(self, fw_perc,d_choke_mm,p_in_atma,p_out_atma,d_pipe_mm=70,t_choke_C=20,c_calibr_fr=1,str_PVT=PVT_DEFAULT,q_gas_sm3day=0):
        """
 ========== description ============== 
  функция расчета дебита жидкости через штуцер   при заданном входном и выходном давлениях 
        
 ==========  arguments  ============== 

     fw_perc - обводненность    

     d_choke_mm - диаметр штуцера (эффективный)    

     p_in_atma - давление на входе (высокой стороне)    

     p_out_atma - давление на выходе (низкой стороне)    

     d_pipe_mm - диаметр трубы до и после штуцера    

     t_choke_c - температура, с.    

     c_calibr_fr - поправочный коэффициент на штуцер  1 - отсутсвие поправки (по умолчанию)  q_choke_real = c_calibr_fr * q_choke_model    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения    

     q_gas_sm3day - дополнительный поток свободного газа   

        """

        self.f_MF_q_choke_sm3day = self.book.macro("MF_q_choke_sm3day")
        return self.f_MF_q_choke_sm3day(fw_perc,d_choke_mm,p_in_atma,p_out_atma,d_pipe_mm,t_choke_C,c_calibr_fr,str_PVT,q_gas_sm3day)

    def PVT_bg_m3m3(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 функция расчета объемного коэффициента газа 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_bg_m3m3 = self.book.macro("PVT_bg_m3m3")
        return self.f_PVT_bg_m3m3(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_bo_m3m3(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет объемного коэффициента нефти 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_bo_m3m3 = self.book.macro("PVT_bo_m3m3")
        return self.f_PVT_bo_m3m3(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_bw_m3m3(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет объемного коэффициента воды 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_bw_m3m3 = self.book.macro("PVT_bw_m3m3")
        return self.f_PVT_bw_m3m3(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_salinity_ppm(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет солености воды 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_salinity_ppm = self.book.macro("PVT_salinity_ppm")
        return self.f_PVT_salinity_ppm(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_mu_oil_cP(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет вязкости нефти 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_mu_oil_cP = self.book.macro("PVT_mu_oil_cP")
        return self.f_PVT_mu_oil_cP(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_mu_gas_cP(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет вязкости газа 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_mu_gas_cP = self.book.macro("PVT_mu_gas_cP")
        return self.f_PVT_mu_gas_cP(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_mu_wat_cP(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет вязкости воды 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_mu_wat_cP = self.book.macro("PVT_mu_wat_cP")
        return self.f_PVT_mu_wat_cP(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_rs_m3m3(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет газосодержания 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_rs_m3m3 = self.book.macro("PVT_rs_m3m3")
        return self.f_PVT_rs_m3m3(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_z(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет коэффициента сверхсжимаемости газа 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_z = self.book.macro("PVT_z")
        return self.f_PVT_z(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_rho_oil_kgm3(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет плотности нефти в рабочих условиях 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_rho_oil_kgm3 = self.book.macro("PVT_rho_oil_kgm3")
        return self.f_PVT_rho_oil_kgm3(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_rho_gas_kgm3(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет плотности газа в рабочих условиях 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_rho_gas_kgm3 = self.book.macro("PVT_rho_gas_kgm3")
        return self.f_PVT_rho_gas_kgm3(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_rho_wat_kgm3(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет плотности воды в рабочих условиях 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_rho_wat_kgm3 = self.book.macro("PVT_rho_wat_kgm3")
        return self.f_PVT_rho_wat_kgm3(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_pb_atma(self, t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 Расчет давления насыщения 
        
 ==========  arguments  ============== 

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_pb_atma = self.book.macro("PVT_pb_atma")
        return self.f_PVT_pb_atma(t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_ST_oilgas_Nm(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет коэффициента поверхностного натяжения нефть - газ 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_ST_oilgas_Nm = self.book.macro("PVT_ST_oilgas_Nm")
        return self.f_PVT_ST_oilgas_Nm(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_ST_watgas_Nm(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет коэффициента поверхностного натяжения вода - газ 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_ST_watgas_Nm = self.book.macro("PVT_ST_watgas_Nm")
        return self.f_PVT_ST_watgas_Nm(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_ST_liqgas_Nm(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет коэффициента поверхностного натяжения жидкость - газ 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_ST_liqgas_Nm = self.book.macro("PVT_ST_liqgas_Nm")
        return self.f_PVT_ST_liqgas_Nm(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_cp_oil_JkgC(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет теплоемкости нефти при постоянном давлении cp 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_cp_oil_JkgC = self.book.macro("PVT_cp_oil_JkgC")
        return self.f_PVT_cp_oil_JkgC(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_cp_gas_JkgC(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет теплоемкости газа при постоянном давлении cp 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_cp_gas_JkgC = self.book.macro("PVT_cp_gas_JkgC")
        return self.f_PVT_cp_gas_JkgC(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_cv_gas_JkgC(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет теплоемкости газа при постоянном давлении cp 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_cv_gas_JkgC = self.book.macro("PVT_cv_gas_JkgC")
        return self.f_PVT_cv_gas_JkgC(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_cp_wat_JkgC(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет теплоемкости воды при постоянном давлении cp 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_cp_wat_JkgC = self.book.macro("PVT_cp_wat_JkgC")
        return self.f_PVT_cp_wat_JkgC(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_compressibility_wat_1atm(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет сжимаемости воды 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_compressibility_wat_1atm = self.book.macro("PVT_compressibility_wat_1atm")
        return self.f_PVT_compressibility_wat_1atm(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_compressibility_oil_1atm(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет сжимаемости нефти 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_compressibility_oil_1atm = self.book.macro("PVT_compressibility_oil_1atm")
        return self.f_PVT_compressibility_oil_1atm(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def PVT_compressibility_gas_1atm(self, p_atma,t_C,gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,str_PVT=""):
        """
 ========== description ============== 
 расчет сжимаемости нефти 
        
 ==========  arguments  ============== 

     p_atma - давление, атм    

     t_c - температура, с.    

     gamma_gas - удельная плотность газа, по воздуху.  const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0 то рассчитается по корреляции    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти, м3/м3.    

     muob_cp - вязкость нефти при давлении насыщения  по умолчанию рассчитывается по корреляции    

     pvtcorr - номер набора pvt корреляций для расчета:  standing_based = 0 - на основе кор-ии стендинга  mccain_based = 1 - на основе кор-ии маккейна  straigth_line = 2 - на основ..см.мануал   

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации доли свободного газа.  изменение свойств нефти зависит от условий  сепарации газа, которы..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения   

        """

        self.f_PVT_compressibility_gas_1atm = self.book.macro("PVT_compressibility_gas_1atm")
        return self.f_PVT_compressibility_gas_1atm(p_atma,t_C,gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,str_PVT)

    def IPR_qliq_sm3day(self, pi_sm3dayatm,pres_atma,Pwf_atma,fw_perc=0,pb_atma=-1):
        """
 ========== description ============== 
 расчет дебита по давлению и продуктивности 
        
 ==========  arguments  ============== 

     pi_sm3dayatm - коэффициент продуктивности, ст.м3/сут/атм    

     pres_atma - пластовое давление, абс. атм    

     pwf_atma - забойное давление, абс. атм    

     fw_perc - обводненность, %    

     pb_atma - давление насыщения, абс. атм   

        """

        self.f_IPR_qliq_sm3day = self.book.macro("IPR_qliq_sm3day")
        return self.f_IPR_qliq_sm3day(pi_sm3dayatm,pres_atma,Pwf_atma,fw_perc,pb_atma)

    def IPR_pwf_atma(self, pi_sm3dayatm,pres_atma,qliq_sm3day,fw_perc=0,pb_atma=-1):
        """
 ========== description ============== 
 расчет забойного давления по дебиту и продуктивности 
        
 ==========  arguments  ============== 

     pi_sm3dayatm - коэффициент продуктивности, ст.м3/сут/атм    

     pres_atma - пластовое давление, абс. атм    

     qliq_sm3day - дебит жидкости скважины на поверхности, ст.м3/сут    

     fw_perc - обводненность, %    

     pb_atma - давление насыщения, абс. атм   

        """

        self.f_IPR_pwf_atma = self.book.macro("IPR_pwf_atma")
        return self.f_IPR_pwf_atma(pi_sm3dayatm,pres_atma,qliq_sm3day,fw_perc,pb_atma)

    def IPR_pi_sm3dayatm(self, Qtest_sm3day,pwf_test_atma,pres_atma,fw_perc=0,pb_atma=-1):
        """
 ========== description ============== 
 расчет коэффициента продуктивности пласта  по данным тестовой эксплуатации 
        
 ==========  arguments  ============== 

     qtest_sm3day - тестовый дебит скважины, ст.м3/сут    

     pwf_test_atma - тестовое забойное давление, абс. атм    

     pres_atma - пластовое давление, абс. атм    

     fw_perc - обводненность, %    

     pb_atma - давление насыщения, абс. атм   

        """

        self.f_IPR_pi_sm3dayatm = self.book.macro("IPR_pi_sm3dayatm")
        return self.f_IPR_pi_sm3dayatm(Qtest_sm3day,pwf_test_atma,pres_atma,fw_perc,pb_atma)

    def ESP_head_m(self, qliq_m3day,num_stages=1,freq_Hz=50,pump_id=674,mu_cSt=-1,c_calibr=1):
        """
 ========== description ============== 
 номинальный напор ЭЦН (на основе каталога ЭЦН)  учитывается поправка на вязкость 
        
 ==========  arguments  ============== 

     qliq_m3day - дебит жидкости в условиях насоса (стенд)    

     num_stages - количество ступеней    

     freq_hz - частота вращения насоса    

     pump_id - номер насоса в базе данных    

     mu_cst - вязкость жидкости, сст;    

     c_calibr - коэффициент поправки на напор.  если массив то второе значение - поправыка на подачу (множитель)  третье на мощность (множитель)   

        """

        self.f_ESP_head_m = self.book.macro("ESP_head_m")
        return self.f_ESP_head_m(qliq_m3day,num_stages,freq_Hz,pump_id,mu_cSt,c_calibr)

    def ESP_power_W(self, qliq_m3day,num_stages=1,freq_Hz=50,pump_id=674,mu_cSt=-1,c_calibr=1):
        """
 ========== description ============== 
 номинальная мощность потребляемая ЭЦН с вала (на основе каталога ЭЦН)  учитывается поправка на вязкость 
        
 ==========  arguments  ============== 

     qliq_m3day - дебит жидкости в условиях насоса (стенд)    

     num_stages - количество ступеней    

     freq_hz - частота вращения насоса    

     pump_id - номер насоса в базе данных    

     mu_cst - вязкость жидкости    

     c_calibr - коэффициент поправки на напор.  если массив то второе значение - поправыка на подачу (множитель)  третье на мощность (множитель)   

        """

        self.f_ESP_power_W = self.book.macro("ESP_power_W")
        return self.f_ESP_power_W(qliq_m3day,num_stages,freq_Hz,pump_id,mu_cSt,c_calibr)

    def ESP_eff_fr(self, qliq_m3day,num_stages=1,freq_Hz=50,pump_id=674,mu_cSt=-1,c_calibr=1):
        """
 ========== description ============== 
 номинальный КПД ЭЦН (на основе каталога ЭЦН)  учитывается поправка на вязкость 
        
 ==========  arguments  ============== 

     qliq_m3day - дебит жидкости в условиях насоса (стенд)    

     num_stages - количество ступеней    

     freq_hz - частота вращения насоса    

     pump_id - номер насоса в базе данных    

     mu_cst - вязкость жидкости    

     c_calibr - коэффициент поправки на напор.  если массив то второе значение - поправыка на подачу (множитель)  третье на мощность (множитель)   

        """

        self.f_ESP_eff_fr = self.book.macro("ESP_eff_fr")
        return self.f_ESP_eff_fr(qliq_m3day,num_stages,freq_Hz,pump_id,mu_cSt,c_calibr)

    def ESP_name(self, pump_id=674):
        """
 ========== description ============== 
 название ЭЦН по номеру 
        
 ==========  arguments  ============== 

     pump_id - идентификатор насоса в базе данных   

        """

        self.f_ESP_name = self.book.macro("ESP_name")
        return self.f_ESP_name(pump_id)

    def ESP_rate_max_sm3day(self, freq_Hz=50,pump_id=674,mu_cSt=-1):
        """
 ========== description ============== 
 максимальный дебит ЭЦН для заданной частоты  по номинальной кривой РНХ 
        
 ==========  arguments  ============== 

     freq_hz - частота вращения эцн    

     pump_id - идентификатор насоса в базе данных    

   mu_cst  

        """

        self.f_ESP_rate_max_sm3day = self.book.macro("ESP_rate_max_sm3day")
        return self.f_ESP_rate_max_sm3day(freq_Hz,pump_id,mu_cSt)

    def ESP_optRate_m3day(self, freq_Hz=50,pump_id=674):
        """
 ========== description ============== 
 оптимальный дебит ЭЦН для заданной частоты  по номинальной кривой РНХ 
        
 ==========  arguments  ============== 

     freq_hz - частота вращения эцн    

     pump_id - идентификатор насоса в базе данных   

        """

        self.f_ESP_optRate_m3day = self.book.macro("ESP_optRate_m3day")
        return self.f_ESP_optRate_m3day(freq_Hz,pump_id)

    def ESP_id_by_rate(self, q):
        """
 ========== description ============== 
 функция возвращает идентификатор типового насоса по значению  номинального дебита 
        
 ==========  arguments  ============== 

     q - номинальный дебит   

        """

        self.f_ESP_id_by_rate = self.book.macro("ESP_id_by_rate")
        return self.f_ESP_id_by_rate(q)

    def ESP_p_atma(self, qliq_sm3day,fw_perc,p_calc_atma,num_stages=1,freq_Hz=50,pump_id=674,str_PVT=PVT_DEFAULT,t_intake_C=50,t_dis_C=50,calc_along_flow=1,ESP_gas_degradation_type=0,c_calibr=1,out_curves_num_points=20,num_value=0):
        """
 ========== description ============== 
функция расчета давления на выходе/входе ЭЦН в рабочих условиях 
        
 ==========  arguments  ============== 

     qliq_sm3day - дебит жидкости на поверхности    

     fw_perc - обводненность    

     p_calc_atma - давление для которого делается расчет  либо давление на приеме насоса  либо давление на выкиде насоса    

     num_stages - количество ступеней    

     freq_hz - частота вращения вала эцн, гц    

     pump_id - идентификатор насоса    

     str_pvt - набор данных pvt    

     t_intake_c - температура на приеме насоа    

     t_dis_c - температура на выкиде насоса.    

     определяется параметром calc_along_flow  num_stages - количество ступеней  freq_hz - частота вращения вала эцн, гц  pump_id - идентификатор насоса  str_pvt - набор данных pvt..см.мануал   

     esp_gas_degradation_type - тип насоса по работе с газом:  0 нет коррекции;  1 стандартный эцн (предел 25%);  2 эцн с газостабилизирующим модулем (предел 50%);  3 эцн с осевым..см.мануал   

     c_calibr - коэффициент поправки на напор.  если массив то второе значение - поправыка на подачу (множитель)  третье на мощность (множитель)    

     out_curves_num_points - количество точек для вывода значений  по ступеня.    

     num_value - значение которое будет выводиться первым   

        """

        self.f_ESP_p_atma = self.book.macro("ESP_p_atma")
        return self.f_ESP_p_atma(qliq_sm3day,fw_perc,p_calc_atma,num_stages,freq_Hz,pump_id,str_PVT,t_intake_C,t_dis_C,calc_along_flow,ESP_gas_degradation_type,c_calibr,out_curves_num_points,num_value)

    def ESP_calibr_pump(self, qliq_sm3day,fw_perc,p_int_atma,p_dis_atma,num_stages=1,freq_Hz=50,pump_id=674,str_PVT=PVT_DEFAULT,t_intake_C=50,t_dis_C=50,calc_along_flow=1,ESP_gas_degradation_type=0,c_calibr=1,calibr_type=0):
        """
 ========== description ============== 
 расчет подстроечных параметров системы УЭЦН 
        
 ==========  arguments  ============== 

     qliq_sm3day - дебит жидкости на поверхности    

     fw_perc - обводненность    

     p_int_atma - давление на приеме насоса    

     p_dis_atma - давление на выкиде насоса    

     num_stages - количество ступеней    

     freq_hz - частота вращения вала эцн, гц    

     pump_id - идентификатор насоса    

     str_pvt - набор данных pvt    

     t_intake_c - температура на приеме насоа    

     t_dis_c - температура на выкиде насоса.    

     если = 0 и calc_along_flow = 1 то рассчитывается  calc_along_flow - режим расчета снизу вверх или сверху вниз  calc_along_flow = true => p_atma давление на приеме  calc_along_..см.мануал   

     esp_gas_degradation_type - тип насоса по работе с газом:  0 нет коррекции;  1 стандартный эцн (предел 25%);  2 эцн с газостабилизирующим модулем (предел 50%);  3 эцн с осевым..см.мануал   

     c_calibr - коэффициент поправки на напор.  если массив то второе значение - поправыка на подачу (множитель)  третье на мощность (множитель)    

     calibr_type - тип калибровки   

        """

        self.f_ESP_calibr_pump = self.book.macro("ESP_calibr_pump")
        return self.f_ESP_calibr_pump(qliq_sm3day,fw_perc,p_int_atma,p_dis_atma,num_stages,freq_Hz,pump_id,str_PVT,t_intake_C,t_dis_C,calc_along_flow,ESP_gas_degradation_type,c_calibr,calibr_type)

    def ESP_system_calc(self, qliq_sm3day,fw_perc,p_calc_atma,str_PVT,str_ESP,calc_along_flow=1,out_curves_num_points=20,num_value=0):
        """
 ========== description ============== 
 расчет производительности системы УЭЦН  считает перепад давления, электрические параметры и деградацию КПД 
        
 ==========  arguments  ============== 

     qliq_sm3day - дебит жидкости на поверхности    

     fw_perc - обводненность    

     p_calc_atma - давление для которого делается расчет  либо давление на приеме насоса  либо давление на выкиде насоса    

     str_pvt - набор данных pvt    

     str_esp - набор данных эцн    

     определяется параметром calc_along_flow  str_pvt - набор данных pvt  str_esp - набор данных эцн  calc_along_flow - режим расчета снизу вверх или сверху вниз  calc_along_flow ..см.мануал   

     out_curves_num_points - количество точек для вывода значений  по ступеня.    

     num_value - значение которое будет выводиться первым   

        """

        self.f_ESP_system_calc = self.book.macro("ESP_system_calc")
        return self.f_ESP_system_calc(qliq_sm3day,fw_perc,p_calc_atma,str_PVT,str_ESP,calc_along_flow,out_curves_num_points,num_value)

    def motor_M_slip_Nm(self, S,freq_Hz=50,U_V=-1,Unom_V=500,Inom_A=10,Fnom_Hz=50,motorID=0):
        """
 ========== description ============== 
 функция расчета момента двигателя от проскальзования 
        
 ==========  arguments  ============== 

     s - скольжение двигателя  опциональные параметры    

     freq_hz - частота вращения внешнего поля    

     u_v - напряжение рабочее, линейное, в    

     unom_v - номинальное напряжение питания двигателя, линейное, в    

     inom_a - номинальный ток двигателя, линейный, а    

     fnom_hz - номинальная частота вращения поля, гц    

     motorid - тип двигателя 0 - задается по схеме замещения,  1 - задается по каталожным кривым  корректно работает, толко для motorid = 0  выход   

        """

        self.f_motor_M_slip_Nm = self.book.macro("motor_M_slip_Nm")
        return self.f_motor_M_slip_Nm(S,freq_Hz,U_V,Unom_V,Inom_A,Fnom_Hz,motorID)

    def motor_I_slip_A(self, S,freq_Hz=50,U_V=-1,Unom_V=500,Inom_A=10,Fnom_Hz=50,motorID=0):
        """
 ========== description ============== 
 Расчет потребляемого тока  погружного ассинхронного двигателя от проскальзывания 
        
 ==========  arguments  ============== 

     s - скольжение двигателя  опциональные параметры    

     freq_hz - частота вращения внешнего поля    

     u_v - напряжение рабочее, линейное, в    

     unom_v - номинальное напряжение питания двигателя, линейное, в    

     inom_a - номинальный ток двигателя, линейный, а    

     fnom_hz - номинальная частота вращения поля, гц    

     motorid - тип двигателя 0 - задается по схеме замещения,  1 - задается по каталожным кривым  корректно работает, толко для motorid = 0  выход   

        """

        self.f_motor_I_slip_A = self.book.macro("motor_I_slip_A")
        return self.f_motor_I_slip_A(S,freq_Hz,U_V,Unom_V,Inom_A,Fnom_Hz,motorID)

    def motor_CosPhi_slip(self, S,freq_Hz=50,U_V=-1,Unom_V=500,Inom_A=10,Fnom_Hz=50,motorID=0):
        """
 ========== description ============== 
 Расчет коэффициента мощности  погружного ассинхронного двигателя от проскальзывания 
        
 ==========  arguments  ============== 

     s - скольжение двигателя  опциональные параметры    

     freq_hz - частота вращения внешнего поля    

     u_v - напряжение рабочее, линейное, в    

     unom_v - номинальное напряжение питания двигателя, линейное, в    

     inom_a - номинальный ток двигателя, линейный, а    

     fnom_hz - номинальная частота вращения поля, гц    

     motorid - тип двигателя 0 - задается по схеме замещения,  1 - задается по каталожным кривым  корректно работает, толко для motorid = 0  выход   

        """

        self.f_motor_CosPhi_slip = self.book.macro("motor_CosPhi_slip")
        return self.f_motor_CosPhi_slip(S,freq_Hz,U_V,Unom_V,Inom_A,Fnom_Hz,motorID)

    def motor_Eff_slip(self, S,freq_Hz=50,U_V=-1,Unom_V=500,Inom_A=10,Fnom_Hz=50,motorID=0):
        """
 ========== description ============== 
 Расчет КПД погружного ассинхронного двигателя от проскальзывания 
        
 ==========  arguments  ============== 

     s - скольжение двигателя  опциональные параметры    

     freq_hz - частота вращения внешнего поля    

     u_v - напряжение рабочее, линейное, в    

     unom_v - номинальное напряжение питания двигателя, линейное, в    

     inom_a - номинальный ток двигателя, линейный, а    

     fnom_hz - номинальная частота вращения поля, гц    

     motorid - тип двигателя 0 - задается по схеме замещения,  1 - задается по каталожным кривым  корректно работает, толко для motorid = 0  выход   

        """

        self.f_motor_Eff_slip = self.book.macro("motor_Eff_slip")
        return self.f_motor_Eff_slip(S,freq_Hz,U_V,Unom_V,Inom_A,Fnom_Hz,motorID)

    def motor_M_Nm(self, Pshaft_kW,freq_Hz=50,U_V=-1,Unom_V=500,Inom_A=10,Fnom_Hz=50,motorID=0):
        """
 ========== description ============== 
 функция расчета момента двигателя от мощности на валу 
        
 ==========  arguments  ============== 

     pshaft_kw - мощность развиваемая двигателем на валу  опциональные параметры    

     freq_hz - частота вращения внешнего поля    

     u_v - напряжение рабочее, линейное, в    

     unom_v - номинальное напряжение питания двигателя, линейное, в    

     inom_a - номинальный ток двигателя, линейный, а    

     fnom_hz - номинальная частота вращения поля, гц    

     motorid - тип двигателя 0 - задается по схеме замещения,  1 - задается по каталожным кривым  выход   

        """

        self.f_motor_M_Nm = self.book.macro("motor_M_Nm")
        return self.f_motor_M_Nm(Pshaft_kW,freq_Hz,U_V,Unom_V,Inom_A,Fnom_Hz,motorID)

    def motor_I_A(self, Pshaft_kW,freq_Hz=50,U_V=-1,Unom_V=500,Inom_A=10,Fnom_Hz=50,motorID=0):
        """
 ========== description ============== 
 функция расчета рабочего тока двигателя 
        
 ==========  arguments  ============== 

     pshaft_kw - мощность развиваемая двигателем на валу  опциональные параметры    

     freq_hz - частота вращения внешнего поля    

     u_v - напряжение рабочее, линейное, в    

     unom_v - номинальное напряжение питания двигателя, линейное, в    

     inom_a - номинальный ток двигателя, линейный, а    

     fnom_hz - номинальная частота вращения поля, гц    

     motorid - тип двигателя 0 - задается по схеме замещения,  1 - задается по каталожным кривым  выход  число - значение тока при данном режиме работы   

        """

        self.f_motor_I_A = self.book.macro("motor_I_A")
        return self.f_motor_I_A(Pshaft_kW,freq_Hz,U_V,Unom_V,Inom_A,Fnom_Hz,motorID)

    def motor_CosPhi_d(self, Pshaft_kW,freq_Hz=50,U_V=-1,Unom_V=500,Inom_A=10,Fnom_Hz=50,motorID=0):
        """
 ========== description ============== 
 функция расчета коэффициента мощности двигателя 
        
 ==========  arguments  ============== 

     pshaft_kw - мощность развиваемая двигателем на валу  опциональные параметры    

     freq_hz - частота вращения внешнего поля    

     u_v - напряжение рабочее, линейное, в    

     unom_v - номинальное напряжение питания двигателя, линейное, в    

     inom_a - номинальный ток двигателя, линейный, а    

     fnom_hz - номинальная частота вращения поля, гц    

     motorid - тип двигателя 0 - задается по схеме замещения,  1 - задается по каталожным кривым  выход   

        """

        self.f_motor_CosPhi_d = self.book.macro("motor_CosPhi_d")
        return self.f_motor_CosPhi_d(Pshaft_kW,freq_Hz,U_V,Unom_V,Inom_A,Fnom_Hz,motorID)

    def motor_Eff_d(self, Pshaft_kW,freq_Hz=50,U_V=-1,Unom_V=500,Inom_A=10,Fnom_Hz=50,motorID=0):
        """
 ========== description ============== 
 функция расчета КПД двигателя 
        
 ==========  arguments  ============== 

     pshaft_kw - мощность развиваемая двигателем на валу  опциональные параметры    

     freq_hz - частота вращения внешнего поля    

     u_v - напряжение рабочее, линейное, в    

     unom_v - номинальное напряжение питания двигателя, линейное, в    

     inom_a - номинальный ток двигателя, линейный, а    

     fnom_hz - номинальная частота вращения поля, гц    

     motorid - тип двигателя 0 - задается по схеме замещения,  1 - задается по каталожным кривым  выход   

        """

        self.f_motor_Eff_d = self.book.macro("motor_Eff_d")
        return self.f_motor_Eff_d(Pshaft_kW,freq_Hz,U_V,Unom_V,Inom_A,Fnom_Hz,motorID)

    def motor_S_d(self, Pshaft_kW,freq_Hz=50,U_V=-1,Unom_V=500,Inom_A=10,Fnom_Hz=50,motorID=0):
        """
 ========== description ============== 
функция расчета скольжения от мощности на валу 
        
 ==========  arguments  ============== 

     pshaft_kw - мощность развиваемая двигателем на валу  опциональные параметры    

     freq_hz - частота вращения внешнего поля    

     u_v - напряжение рабочее, линейное, в    

     unom_v - номинальное напряжение питания двигателя, линейное, в    

     inom_a - номинальный ток двигателя, линейный, а    

     fnom_hz - номинальная частота вращения поля, гц    

     motorid - тип двигателя 0 - задается по схеме замещения,  1 - задается по каталожным кривым  выход   

        """

        self.f_motor_S_d = self.book.macro("motor_S_d")
        return self.f_motor_S_d(Pshaft_kW,freq_Hz,U_V,Unom_V,Inom_A,Fnom_Hz,motorID)

    def motor_Name(self, Unom_V=500,Inom_A=10,Fnom_Hz=50,motorID=0):
        """
 ========== description ============== 
 функция выдает название двигателя по его характеристикам 
        
 ==========  arguments  ============== 

     unom_v - номинальное напряжение питания двигателя, линейное, в    

     inom_a - номинальный ток двигателя, линейный, а    

     fnom_hz - номинальная частота вращения поля, гц    

     motorid - тип двигателя 0 - задается по схеме замещения,  1 - задается по каталожным кривым выход   

        """

        self.f_motor_Name = self.book.macro("motor_Name")
        return self.f_motor_Name(Unom_V,Inom_A,Fnom_Hz,motorID)

    def motor_Pnom_kW(self, Unom_V=500,Inom_A=10,Fnom_Hz=50,motorID=0):
        """
 ========== description ============== 
 функция выдает номинальную мощность ПЭД по его характеристикам 
        
 ==========  arguments  ============== 

     unom_v - номинальное напряжение питания двигателя, линейное, в    

     inom_a - номинальный ток двигателя, линейный, а    

     fnom_hz - номинальная частота вращения поля, гц    

     motorid - тип двигателя 0 - задается по схеме замещения,  1 - задается по каталожным кривым выход   

        """

        self.f_motor_Pnom_kW = self.book.macro("motor_Pnom_kW")
        return self.f_motor_Pnom_kW(Unom_V,Inom_A,Fnom_Hz,motorID)

    def ESP_ksep_gasseparator_d(self, gsep_type_TYPE,gas_frac_d,qliq_sm3day,freq_Hz=50):
        """
 ========== description ============== 
 расчет коэффициента сепарации газосепаратора  по результатам стендовых испытаний РГУ нефти и газа 
        
 ==========  arguments  ============== 

     gsep_type_type - тип сепаратора (номер от 1 до 29)    

     gas_frac_d - газосодержание на входе в газосепаратор    

     qliq_sm3day - дебит жидкости в стандартных условиях    

     freq_hz - частота врашения, гц   

        """

        self.f_ESP_ksep_gasseparator_d = self.book.macro("ESP_ksep_gasseparator_d")
        return self.f_ESP_ksep_gasseparator_d(gsep_type_TYPE,gas_frac_d,qliq_sm3day,freq_Hz)

    def ESP_gasseparator_name(self, gsep_type_TYPE):
        """
 ========== description ============== 
 название газосопаратора 
        
 ==========  arguments  ============== 

     gsep_type_type - тип сепаратора (номер от 1 до 29)   

        """

        self.f_ESP_gasseparator_name = self.book.macro("ESP_gasseparator_name")
        return self.f_ESP_gasseparator_name(gsep_type_TYPE)

    def GLV_q_gas_sm3day(self, d_mm,p_in_atma,p_out_atma,gamma_g,t_C,c_calibr=1):
        """
 ========== description ============== 
 функция расчета расхода газа через газлифтный клапан/штуцер  результат массив значений и подписей 
        
 ==========  arguments  ============== 

     d_mm - диаметр основного порта клапана, мм    

     p_in_atma - давление на входе в клапан (затруб), атма    

     p_out_atma - давление на выходе клапана (нкт), атма    

     gamma_g - удельная плотность газа    

     t_c - температура клапана, с    

   c_calibr  

        """

        self.f_GLV_q_gas_sm3day = self.book.macro("GLV_q_gas_sm3day")
        return self.f_GLV_q_gas_sm3day(d_mm,p_in_atma,p_out_atma,gamma_g,t_C,c_calibr)

    def GLV_q_gas_vkr_sm3day(self, d_port_mm,d_vkr_mm,p_in_atma,p_out_atma,gamma_g,t_C):
        """
 ========== description ============== 
 функция расчета расхода газа через газлифтный клапан  с учетом наличия вкруток на выходе клапана.  результат массив значений и подписей. 
        
 ==========  arguments  ============== 

     d_port_mm - диаметр основного порта клапана, мм    

     d_vkr_mm - эффективный диаметр вкруток на выходе, мм    

     p_in_atma - давление на входе в клапан (затруб), атма    

     p_out_atma - давление на выходе клапана (нкт), атма    

     gamma_g - удельная плотность газа    

     t_c - температура клапана, с   

        """

        self.f_GLV_q_gas_vkr_sm3day = self.book.macro("GLV_q_gas_vkr_sm3day")
        return self.f_GLV_q_gas_vkr_sm3day(d_port_mm,d_vkr_mm,p_in_atma,p_out_atma,gamma_g,t_C)

    def GLV_p_vkr_atma(self, d_port_mm,d_vkr_mm,p_calc_atma,q_gas_sm3day,gamma_g=0.6,t_C=25,calc_along_flow=False):
        """
 ========== description ============== 
 функция расчета давления на входе или на выходе  газлифтного клапана (простого) при закачке газа.  результат массив значений и подписей 
        
 ==========  arguments  ============== 

     d_port_mm - диаметр порта клапана, мм    

     d_vkr_mm - диаметр вкрутки клапана, мм    

     p_calc_atma - давление на входе (выходе) клапана, атма    

     q_gas_sm3day - расход газа, ст. м3/сут    

     gamma_g - удельная плотность газа    

     t_c - температура в точке установки клапана    

     calc_along_flow - направление расчета:  0 - против потока (расчет давления на входе);  1 - по потоку (расчет давления на выходе).   

        """

        self.f_GLV_p_vkr_atma = self.book.macro("GLV_p_vkr_atma")
        return self.f_GLV_p_vkr_atma(d_port_mm,d_vkr_mm,p_calc_atma,q_gas_sm3day,gamma_g,t_C,calc_along_flow)

    def GLV_p_atma(self, d_mm,p_calc_atma,q_gas_sm3day,gamma_g=0.6,t_C=25,calc_along_flow=False,p_open_atma=0,c_calibr=1):
        """
 ========== description ============== 
 функция расчета давления на входе или на выходе  газлифтного клапана (простого) при закачке газа.  результат массив значений и подписей 
        
 ==========  arguments  ============== 

     d_mm - диаметр клапана, мм    

     p_calc_atma - давление на входе (выходе) клапана, атма    

     q_gas_sm3day - расход газа, ст. м3/сут    

     gamma_g - удельная плотность газа    

     t_c - температура в точке установки клапана    

     calc_along_flow - направление расчета:  0 - против потока (расчет давления на входе);  1 - по потоку (расчет давления на выходе).    

     p_open_atma - давление открытия/закрытия клапана, атм    

   c_calibr  

        """

        self.f_GLV_p_atma = self.book.macro("GLV_p_atma")
        return self.f_GLV_p_atma(d_mm,p_calc_atma,q_gas_sm3day,gamma_g,t_C,calc_along_flow,p_open_atma,c_calibr)

    def GLV_p_bellow_atma(self, p_atma,t_C):
        """
 ========== description ============== 
 функция расчета давления зарядки сильфона на стенде при  стандартной температуре по данным рабочих давления и температуры 
        
 ==========  arguments  ============== 

     p_atma - рабочее давление открытия клапана в скважине, атм    

     t_c - рабочая температура открытия клапана в скважине, с   

        """

        self.f_GLV_p_bellow_atma = self.book.macro("GLV_p_bellow_atma")
        return self.f_GLV_p_bellow_atma(p_atma,t_C)

    def GLV_p_close_atma(self, p_bellow_atm,t_C):
        """
 ========== description ============== 
 фукнция расчета давления в сильфоне с азотом  в рабочих условиях при заданной температуре 
        
 ==========  arguments  ============== 

     p_bellow_atm - давление зарядки сильфона при стандартных условиях    

     t_c - температура рабочая   

        """

        self.f_GLV_p_close_atma = self.book.macro("GLV_p_close_atma")
        return self.f_GLV_p_close_atma(p_bellow_atm,t_C)

    def GLV_d_choke_mm(self, q_gas_sm3day,p_in_atma,p_out_atma,gamma_g=0.6,t_C=25):
        """
 ========== description ============== 
Функция расчета диаметра порта клапана на основе уравнения Thornhill-Crave 
        
 ==========  arguments  ============== 

     q_gas_sm3day - расход газа, ст. м3/сут    

     p_in_atma - давление на входе в клапан (затруб), атма    

     p_out_atma - давление на выходе клапана (нкт), атма    

     gamma_g - удельная плотность газа    

     t_c - температура клапана, с   

        """

        self.f_GLV_d_choke_mm = self.book.macro("GLV_d_choke_mm")
        return self.f_GLV_d_choke_mm(q_gas_sm3day,p_in_atma,p_out_atma,gamma_g,t_C)

    def GLV_IPO_p_open(self, p_bellow_atma,p_out_atma,t_C,GLV_type=0,d_port_mm=5,d_vkr1_mm=-1,d_vkr2_mm=-1,d_vkr3_mm=-1,d_vkr4_mm=-1):
        """
 ========== description ============== 
Функция расчета давления открытия газлифтного клапана R1 
        
 ==========  arguments  ============== 

     p_bellow_atma - давление зарядки сильфона на стенде, атма    

     p_out_atma - давление на выходе клапана (нкт), атма    

     t_c - температура клапана в рабочих условиях, с    

     glv_type - тип газлифтного клапана (сейчас только r1)    

     d_port_mm - диаметр порта клапана    

     d_vkr1_mm - диаметр вкрутки 1, если есть    

     d_vkr2_mm - диаметр вкрутки 2, если есть    

     d_vkr3_mm - диаметр вкрутки 3, если есть    

     d_vkr4_mm - диаметр вкрутки 4, если есть   

        """

        self.f_GLV_IPO_p_open = self.book.macro("GLV_IPO_p_open")
        return self.f_GLV_IPO_p_open(p_bellow_atma,p_out_atma,t_C,GLV_type,d_port_mm,d_vkr1_mm,d_vkr2_mm,d_vkr3_mm,d_vkr4_mm)

    def GLV_IPO_p_atma(self, p_bellow_atma,d_port_mm,p_calc_atma,q_gas_sm3day,t_C,calc_along_flow=False,GLV_type=0,d_vkr1_mm=-1,d_vkr2_mm=-1,d_vkr3_mm=-1,d_vkr4_mm=-1):
        """
 ========== description ============== 
Функция расчета давления открытия газлифтного клапана R1 
        
 ==========  arguments  ============== 

     p_bellow_atma - давление зарядки сильфона на стенде, атма  p_out_atma - давление на выходе клапана (нкт), атма    

     d_port_mm - диаметр порта клапана    

   p_calc_atma   

   q_gas_sm3day   

     t_c - температура клапана в рабочих условиях, с    

   calc_along_flow   

     glv_type - тип газлифтного клапана (сейчас только r1)  d_port_mm - диаметр порта клапана    

     d_vkr1_mm - диаметр вкрутки 1, если есть    

     d_vkr2_mm - диаметр вкрутки 2, если есть    

     d_vkr3_mm - диаметр вкрутки 3, если есть    

     d_vkr4_mm - диаметр вкрутки 4, если есть   

        """

        self.f_GLV_IPO_p_atma = self.book.macro("GLV_IPO_p_atma")
        return self.f_GLV_IPO_p_atma(p_bellow_atma,d_port_mm,p_calc_atma,q_gas_sm3day,t_C,calc_along_flow,GLV_type,d_vkr1_mm,d_vkr2_mm,d_vkr3_mm,d_vkr4_mm)

    def GLV_IPO_p_close(self, p_bellow_atma,p_out_atma,t_C,GLV_type=0,d_port_mm=5,d_vkr1_mm=-1,d_vkr2_mm=-1,d_vkr3_mm=-1,d_vkr4_mm=-1):
        """
 ========== description ============== 
Функция расчета давления закрытия газлифтного клапана R1 
        
 ==========  arguments  ============== 

     p_bellow_atma - давление зарядки сильфона на стенде, атма    

     p_out_atma - давление на выходе клапана (нкт), атма    

     t_c - температура клапана в рабочих условиях, с    

     glv_type - тип газлифтного клапана (сейчас только r1)    

     d_port_mm - диаметр порта клапана    

     d_vkr1_mm - диаметр вкрутки 1, если есть    

     d_vkr2_mm - диаметр вкрутки 2, если есть    

     d_vkr3_mm - диаметр вкрутки 3, если есть    

     d_vkr4_mm - диаметр вкрутки 4, если есть   

        """

        self.f_GLV_IPO_p_close = self.book.macro("GLV_IPO_p_close")
        return self.f_GLV_IPO_p_close(p_bellow_atma,p_out_atma,t_C,GLV_type,d_port_mm,d_vkr1_mm,d_vkr2_mm,d_vkr3_mm,d_vkr4_mm)

    def unf_version(self, ):
        """
 ========== description ============== 
 функция возвращает номер версии Унифлок VBA 
        
 ==========  arguments  ============== 

     

        """

        self.f_unf_version = self.book.macro("unf_version")
        return self.f_unf_version()

    def PVT_encode_string(self, gamma_gas=const_gg_,gamma_oil=const_go_,gamma_wat=const_gw_,rsb_m3m3=const_rsb_default,rp_m3m3=-1,pb_atma=-1,tres_C=const_tres_default,bob_m3m3=-1,muob_cP=-1,PVTcorr=Standing_based,ksep_fr=0,p_ksep_atma=-1,t_ksep_C=-1,gas_only=False):
        """
 ========== description ============== 
 Функция кодирования параметров PVT в строку,  для передачи PVT свойств в прикладные функции Унифлок. 
        
 ==========  arguments  ============== 

     gamma_gas - удельная плотность газа, по воздуху.  по умолчанию const_gg_ = 0.6    

     gamma_oil - удельная плотность нефти, по воде.  по умолчанию const_go_ = 0.86    

     gamma_wat - удельная плотность воды, по воде.  по умолчанию const_gw_ = 1    

     rsb_m3m3 - газосодержание при давлении насыщения, м3/м3.  по умолчанию const_rsb_default = 100    

     rp_m3m3 - замерной газовый фактор, м3/м3.  имеет приоритет перед rsb если rp < rsb    

     pb_atma - давление насыщения при температуре пласта, атма.  опциональный калибровочный параметр,  если не задан или = 0, то рассчитается по корреляции.    

     tres_c - пластовая температура, с.  учитывается при расчете давления насыщения.  по умолчанию const_tres_default = 90    

     bob_m3m3 - объемный коэффициент нефти при давлении насыщения  и пластовой температуре, м3/м3.  по умолчанию рассчитывается по корреляции.    

     muob_cp - вязкость нефти при давлении насыщения.  и пластовой температуре, сп.  по умолчанию рассчитывается по корреляции.    

     pvtcorr - номер набора pvt корреляций для расчета:  0 - на основе корреляции стендинга;  1 - на основе кор-ии маккейна;  2 - на основе упрощенных зависимостей.    

     ksep_fr - коэффициент сепарации - определяет изменение свойств  нефти после сепарации части свободного газа.  зависит от давления и температуры  сепарации газа, которые должны..см.мануал   

     p_ksep_atma - давление при которой была сепарация    

     t_ksep_c - температура при которой была сепарация    

     gas_only - флаг - в потоке только газ  по умолчанию false (нефть вода и газ)   

        """

        self.f_PVT_encode_string = self.book.macro("PVT_encode_string")
        return self.f_PVT_encode_string(gamma_gas,gamma_oil,gamma_wat,rsb_m3m3,rp_m3m3,pb_atma,tres_C,bob_m3m3,muob_cP,PVTcorr,ksep_fr,p_ksep_atma,t_ksep_C,gas_only)

    def PVT_decode_string(self, str_PVT=PVT_DEFAULT,getStr=False):
        """
 ========== description ============== 
 функция расшифровки параметров PVT закодированных в строке 
        
 ==========  arguments  ============== 

     str_pvt - строка с параметрами pvt    

     getstr - флаг проверки работы функции  по умолчанию false (0) - функция выдает объект cpvt  если задать true - функция раскодирует строку и снова закодирует  и выдаст строку (..см.мануал  

        """

        self.f_PVT_decode_string = self.book.macro("PVT_decode_string")
        return self.f_PVT_decode_string(str_PVT,getStr)

    def ESP_encode_string(self, esp_ID=1005,HeadNom_m=2000,ESPfreq_Hz=50,ESP_U_V=1000,MotorPowerNom_kW=30,t_intake_C=85,t_dis_C=85,KsepGS_fr=0,ksep_manual_fr=0,ESP_energy_fact_Whday=0,ESP_cable_type=0,ESP_h_mes_m=0,ESP_gas_degradation_type=0,c_calibr=1,PKV_work_min=-1,PKV_stop_min=-1):
        """
 ========== description ============== 
 функция кодирования параметров работы УЭЦН в строку,  которую можно потом использовать для задания ЭЦН в прикладных функциях 
        
 ==========  arguments  ============== 

     esp_id - идентификатор насоса    

     headnom_m - номинальный напор системы уэцн  - соответствует напора в записи эцн 50-2000    

     espfreq_hz - частота, гц    

     esp_u_v - напряжение на пэд    

     motorpowernom_kw - номинальная мощность двигателя    

     t_intake_c - температура на приеме насоа    

     t_dis_c - температура на выкиде насоса.  если = 0 и calc_along_flow = 1 то рассчитывается    

     ksepgs_fr - коэффициент сепарации газосепаратора уэцн    

   ksep_manual_fr   

     esp_energy_fact_whday - фактическое потребление мощности эцн    

     esp_cable_type - тип кабельной линии  тип 1: cable_r_omkm = 1.18  cable_name = кппапбп-120 3x16  cable_tmax_c = 120    

     esp_h_mes_m - длина кабельной линии    

     esp_gas_degradation_type - тип насоса по работе с газом  0 - нет коррекции,  1 - стандартный эцн (предел 25%),  2 - эцн с газостабилизирующим модулем (предел 50%),  3 - эцн с..см.мануал   

     c_calibr - коэффициент поправки на напор.  если массив то второе значение - поправыка на подачу (множитель)  третье на мощность (множитель)    

     pkv_work_min - время работы скважины для режима пкв в минутах    

     pkv_stop_min - время ожидания запуска скважины для пкв , мин  пкв - периодическое кратковременное включение  если не заданы, то скважина в пдф  пдф - постоянно действующий фон..см.мануал  

        """

        self.f_ESP_encode_string = self.book.macro("ESP_encode_string")
        return self.f_ESP_encode_string(esp_ID,HeadNom_m,ESPfreq_Hz,ESP_U_V,MotorPowerNom_kW,t_intake_C,t_dis_C,KsepGS_fr,ksep_manual_fr,ESP_energy_fact_Whday,ESP_cable_type,ESP_h_mes_m,ESP_gas_degradation_type,c_calibr,PKV_work_min,PKV_stop_min)

    def ESP_decode_string(self, str_ESP,getStr=False):
        """
 ========== description ============== 
 функция расшифровки параметров работы ЭЦН закодированных в строке 
        
 ==========  arguments  ============== 

     str_esp - строка с параметрами эцн    

     getstr - флаг проверки работы функции  по умолчанию false (0) - функция выдает объект cespsystemsimple  если задать true - функция раскодирует строку и снова закодирует  и выд..см.мануал  

        """

        self.f_ESP_decode_string = self.book.macro("ESP_decode_string")
        return self.f_ESP_decode_string(str_ESP,getStr)

    def GL_decode_string(self, well_GL_str,getStr=False):
        """
 ========== description ============== 
 функция расшифровки параметров газлифтной компоновки скважины 
        
 ==========  arguments  ============== 

     well_gl_str - строка с параметрами газлифтной скважины    

     getstr - флаг проверки работы функции  по умолчанию false (0) - функция выдает объект cespsystemsimple  если задать true - функция раскодирует строку и снова закодирует  и выд..см.мануал  

        """

        self.f_GL_decode_string = self.book.macro("GL_decode_string")
        return self.f_GL_decode_string(well_GL_str,getStr)

    def GL_encode_string(self, q_gas_inj_sm3day=0,p_gas_inj_atma=0,d_gas_inj_mm=0,HmesGLV_m=0,dGLV_mm=0,PsurfGLV_atma=0):
        """
 ========== description ============== 
 функция кодирования параметров работы скважины с газлифтом 
        
 ==========  arguments  ============== 

     q_gas_inj_sm3day - расход газа закачки    

     p_gas_inj_atma - давление газа закачки на поверхности    

     d_gas_inj_mm - диаметр штуцера регулировки закачки газа на поверхности    

     hmesglv_m - измеренные глубины установки газлифтных клапанов    

     dglv_mm - диаметры порта установленных газлифтных клапанов    

     psurfglv_atma - давления зарядки газлифтных клапанов   

        """

        self.f_GL_encode_string = self.book.macro("GL_encode_string")
        return self.f_GL_encode_string(q_gas_inj_sm3day,p_gas_inj_atma,d_gas_inj_mm,HmesGLV_m,dGLV_mm,PsurfGLV_atma)

    def well_plin_pwf_atma(self, qliq_sm3day,fw_perc,Pwf_atma,h_perf_m,pcas_atma,d_choke_mm,str_PVT=PVT_DEFAULT,str_AL="",hmes_habs_list_m=0,dtub_list_mm=0,dcas_list_mm=0,temp_list_C=0,hydr_corr=H_CORRELATION,temp_methodTEMP_CALC_METHOD=StartEndTemp,twf_C=0,c_calibr_grav=1,c_calibr_fric=1,c_calibr_choke=1,q_gas_sm3day=0,param_out=1,num_pt_crv=21):
        """
 ========== description ============== 
 Расчет устьевого давления скважины,  расчет распределения давления и температуры в скважине  с использованием многофазных корреляций. 
        
 ==========  arguments  ============== 

     qliq_sm3day - дебит жидкости в поверхностных условиях    

     fw_perc - обводненность    

     pwf_atma - забойное давление с которого начинается расчет, атм  граничное значение для проведения расчета    

     h_perf_m - измеренная глубина пласта (перфорации)  точка узлового анализа при узле на забое скважины    

     pcas_atma - затрубное давление (расчета ндин)    

     d_choke_mm - диаметр штуцера    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения    

     str_al - закодированная параметров мех добычи.  строка параметров эцн либо строка параметров газлифта    

     hmes_habs_list_m -траектория скважины. range или таблица [0..n,0..1]    

     dtub_list_mm - диаметр нкт. range или таблица [0..n,0..1]    

     dcas_list_mm - диаметр эксп колонны. range или таблица [0..n,0..1]    

     temp_list_c - температура среды. range или таблица [0..n,0..1]    

     hydr_corr - гидравлическая корреляция, h_correlation  beggsbrill = 0  ansari = 1  unified = 2  gray = 3  hagedornbrown = 4  sakharovmokhov = 5    

     temp_method - температурная модель    

     twf_c - температура флюида на забое  необходима для продвинутого учета температуры    

     c_calibr_grav - поправка на гравитационную составляющую  перепада давления    

     c_calibr_fric - поправка на трение в перепаде давления    

     c_calibr_choke - поправка на штуцер    

     q_gas_sm3day - свободный газ поступающие в трубу.    

     param_out - номер параметра для вывода в ячейку [0,0]    

     num_pt_crv - число параметров вывода массивов   

        """

        self.f_well_plin_pwf_atma = self.book.macro("well_plin_pwf_atma")
        return self.f_well_plin_pwf_atma(qliq_sm3day,fw_perc,Pwf_atma,h_perf_m,pcas_atma,d_choke_mm,str_PVT,str_AL,hmes_habs_list_m,dtub_list_mm,dcas_list_mm,temp_list_C,hydr_corr,temp_method,twf_C,c_calibr_grav,c_calibr_fric,c_calibr_choke,q_gas_sm3day,param_out,num_pt_crv)

    def well_pwf_plin_atma(self, qliq_sm3day,fw_perc,plin_atma,h_perf_m,pcas_atma,d_choke_mm,str_PVT=PVT_DEFAULT,str_AL="",hmes_habs_list_m=0,dtub_list_mm=0,dcas_list_mm=0,temp_list_C=0,hydr_corr=H_CORRELATION,temp_methodTEMP_CALC_METHOD=StartEndTemp,twf_C=0,c_calibr_grav=1,c_calibr_fric=1,c_calibr_choke=1,q_gas_sm3day=0,param_out=6,num_pt_crv=21):
        """
 ========== description ============== 
 Расчет забойного давления скважины,  расчет распределения давления и температуры в скважине  с использованием многофазных корреляций 
        
 ==========  arguments  ============== 

     qliq_sm3day - дебит жидкости в поверхностных условиях    

     fw_perc - обводненность    

     plin_atma - линейное давление с которого начинается расчет, атм  граничное значение для проведения расчета    

     h_perf_m - измеренная глубина пласта (перфорации)  точка узлового анализа при узле на забое скважины    

     pcas_atma - затрубное давление (расчета ндин)    

     d_choke_mm - диаметр штуцера    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения    

     str_al - закодированная параметров мех добычи.  строка параметров эцн либо строка параметров газлифта    

     hmes_habs_list_m -траектория скважины. range или таблица [0..n,0..1]    

     dtub_list_mm - диаметр нкт. range или таблица [0..n,0..1]    

     dcas_list_mm - диаметр эксп колонны. range или таблица [0..n,0..1]    

     temp_list_c - температура среды. range или таблица [0..n,0..1]    

     hydr_corr - гидравлическая корреляция, h_correlation  beggsbrill = 0  ansari = 1  unified = 2  gray = 3  hagedornbrown = 4  sakharovmokhov = 5    

     temp_method - температурная модель    

   twf_c   

     c_calibr_grav - поправка на гравитационную составляющую  перепада давления    

     c_calibr_fric - поправка на трение в перепаде давления    

     c_calibr_choke - поправка на штуцер  roughness_m - шероховатость трубы    

     q_gas_sm3day - свободный газ поступающие в трубу.    

     param_out - номер параметра для вывода в ячейку [0,0]    

     num_pt_crv - число параметров вывода массивов   

        """

        self.f_well_pwf_plin_atma = self.book.macro("well_pwf_plin_atma")
        return self.f_well_pwf_plin_atma(qliq_sm3day,fw_perc,plin_atma,h_perf_m,pcas_atma,d_choke_mm,str_PVT,str_AL,hmes_habs_list_m,dtub_list_mm,dcas_list_mm,temp_list_C,hydr_corr,temp_method,twf_C,c_calibr_grav,c_calibr_fric,c_calibr_choke,q_gas_sm3day,param_out,num_pt_crv)

    def wellESP_plin_pintake_atma(self, qliq_sm3day,fw_perc,pintake_atma,h_perf_m,pcas_atma,d_choke_mm,str_PVT=PVT_DEFAULT,str_AL="",hmes_habs_list_m=0,dtub_list_mm=0,dcas_list_mm=0,temp_list_C=0,hydr_corr=H_CORRELATION,temp_methodTEMP_CALC_METHOD=StartEndTemp,twf_C=0,c_calibr_grav=1,c_calibr_fric=1,c_calibr_choke=1,q_gas_sm3day=0,param_out=1,num_pt_crv=21):
        """
 ========== description ============== 
 Расчет устьевого давления скважины по давлению на приеме.  Расчет распределения давления и температуры в скважине  с использованием многофазных корреляций. 
        
 ==========  arguments  ============== 

     qliq_sm3day - дебит жидкости в поверхностных условиях    

     fw_perc - обводненность    

     pintake_atma- давление на приеме с которого начинается расчет, атм  граничное значение для проведения расчета    

     h_perf_m - измеренная глубина пласта (перфорации)  точка узлового анализа при узле на забое скважины    

     pcas_atma - затрубное давление (расчета ндин)    

     d_choke_mm - диаметр штуцера    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения    

     str_al - закодированная параметров мех добычи.  строка параметров эцн либо строка параметров газлифта    

     hmes_habs_list_m - траектория скважины. range или таблица [0..n,0..1]    

     dtub_list_mm - диаметр нкт. range или таблица [0..n,0..1]    

     dcas_list_mm - диаметр эксп колонны. range или таблица [0..n,0..1]    

     temp_list_c - температура среды. range или таблица [0..n,0..1]    

     hydr_corr - гидравлическая корреляция, h_correlation  beggsbrill = 0  ansari = 1  unified = 2  gray = 3  hagedornbrown = 4  sakharovmokhov = 5    

     temp_method - температурная модель    

     twf_c - температура флюида на забое  необходима для продвинутого учета температуры    

     c_calibr_grav - поправка на гравитационную составляющую  перепада давления    

     c_calibr_fric - поправка на трение в перепаде давления    

     c_calibr_choke - поправка на штуцер  roughness_m - шероховатость трубы    

     q_gas_sm3day - свободный газ поступающие в трубу.    

     param_out - номер параметра для вывода в ячейку [0,0]    

     num_pt_crv - число параметров вывода массивов   

        """

        self.f_wellESP_plin_pintake_atma = self.book.macro("wellESP_plin_pintake_atma")
        return self.f_wellESP_plin_pintake_atma(qliq_sm3day,fw_perc,pintake_atma,h_perf_m,pcas_atma,d_choke_mm,str_PVT,str_AL,hmes_habs_list_m,dtub_list_mm,dcas_list_mm,temp_list_C,hydr_corr,temp_method,twf_C,c_calibr_grav,c_calibr_fric,c_calibr_choke,q_gas_sm3day,param_out,num_pt_crv)

    def nodal_pwf_atma(self, pi_sm3dayatm,pres_atma,fw_perc,h_perf_m,plin_atma,pcas_atma,d_choke_mm,str_PVT=PVT_DEFAULT,str_AL="",hmes_habs_list_m=0,dtub_list_mm=0,dcas_list_mm=0,temp_list_C=0,hydr_corr=H_CORRELATION,temp_methodTEMP_CALC_METHOD=StartEndTemp,twf_C=0,c_calibr_grav=1,c_calibr_fric=1,c_calibr_choke=1,q_gas_sm3day=0,num_pt_crv=21):
        """
 ========== description ============== 
 Расчет забойного давления по узловому анализу,  скважины и пласта. 
        
 ==========  arguments  ============== 

     pi_sm3dayatm - коэффициент продуктивности    

     pres_atma - пластовое давление    

     fw_perc - обводненность  pwf_atma - забойное давление с которого начинается расчет, атм  граничное значение для проведения расчета    

     h_perf_m - измеренная глубина пласта (перфорации)  точка узлового анализа при узле на забое скважины    

   plin_atma   

     pcas_atma - затрубное давление (расчета ндин)    

     d_choke_mm - диаметр штуцера    

     str_pvt - закодированная строка с параметрами pvt.  если задана - перекрывает другие значения    

     str_al - закодированная параметров мех добычи.  строка параметров эцн либо строка параметров газлифта    

     hmes_habs_list_m -траектория скважины. range или таблица [0..n,0..1]    

     dtub_list_mm - диаметр нкт. range или таблица [0..n,0..1]    

     dcas_list_mm - диаметр эксп колонны. range или таблица [0..n,0..1]    

     temp_list_c - температура среды. range или таблица [0..n,0..1]    

     hydr_corr - гидравлическая корреляция, h_correlation  beggsbrill = 0  ansari = 1  unified = 2  gray = 3  hagedornbrown = 4  sakharovmokhov = 5    

     temp_method - температурная модель    

     twf_c - температура флюида на забое  необходима для продвинутого учета температуры    

     c_calibr_grav - поправка на гравитационную составляющую  перепада давления    

     c_calibr_fric - поправка на трение в перепаде давления    

     c_calibr_choke - поправка на штуцер    

     q_gas_sm3day - свободный газ поступающие в трубу.    

     num_pt_crv - число параметров вывода массивов   

        """

        self.f_nodal_pwf_atma = self.book.macro("nodal_pwf_atma")
        return self.f_nodal_pwf_atma(pi_sm3dayatm,pres_atma,fw_perc,h_perf_m,plin_atma,pcas_atma,d_choke_mm,str_PVT,str_AL,hmes_habs_list_m,dtub_list_mm,dcas_list_mm,temp_list_C,hydr_corr,temp_method,twf_C,c_calibr_grav,c_calibr_fric,c_calibr_choke,q_gas_sm3day,num_pt_crv)

    def crv_interpolation(self, x_points,y_points,x_val,type_interpolation=0):
        """
 ========== description ============== 
 функция поиска значения функции по заданным табличным данным (интерполяция) 
        
 ==========  arguments  ============== 

     x_points - таблица аргументов функции    

     y_points - таблица значений функции  количество агрументов и значений функции должно совпадать  для табличной функции одному аргументу соответствует  строго одно значение функ..см.мануал   

     x_val - аргумент для которого надо найти значение  одно значение в ячейке или диапазон значений  для диапазона аргументов будет найден диапазон значений  диапазоны могут быть ..см.мануал   

     type_interpolation - тип интерполяции  0 - линейная интерполяция  1 - кубическая интерполяция  2 - интерполяция акима (выбросы)  www.en.wikipedia.org/wiki/akima_spline  3 - ..см.мануал  

        """

        self.f_crv_interpolation = self.book.macro("crv_interpolation")
        return self.f_crv_interpolation(x_points,y_points,x_val,type_interpolation)

    def crv_interpolation_2D(self, xa,YA,FA,XYIA,out=1,type_interpolation=0):
        """
 ========== description ============== 
 функция поиска значения функции по двумерным табличным данным (интерполяция 2D) 
        
 ==========  arguments  ============== 

     xa - x значения исходных данных (строка значений или массив)    

     ya - y значения исходных данных (столбец значений или массив)    

     fa - табличные значения интерполируемой функции,  двумерная таблица или массив    

     xyia - таблица значений для которой надо найти результат  два столбца значений (x,y) или массив с двумя колонками  если не заданы возвращаются кубические коэффициента для каждо..см.мануал   

     out - для интерполяции кубическими сплайнами  out = 0 возвращаются только значения  out = 1 возвращаются значения и производные    

     type_interpolation - тип интерполяции  0 - линейная интерполяция  1 - кубическая интерполяция   

        """

        self.f_crv_interpolation_2D = self.book.macro("crv_interpolation_2D")
        return self.f_crv_interpolation_2D(xa,YA,FA,XYIA,out,type_interpolation)

    def crv_solve(self, x_points,y_points,y_val):
        """
 ========== description ============== 
 функция решения уравнения в табличном виде f(x) = y_val  ищется значение аргумента соответствующее заданному значению  используется линейная интерполяция  возможно несколько решений 
        
 ==========  arguments  ============== 

     x_points - таблица аргументов функции    

     y_points - таблица значений функции  количество агрументов и значений функции должно совпадать  для табличной функции одному аргументу соответствует  строго одно значение функ..см.мануал   

     y_val - значение функции для которого надо ищутся аргументы  строго одно вещественное число (ссылка на ячейку)   

        """

        self.f_crv_solve = self.book.macro("crv_solve")
        return self.f_crv_solve(x_points,y_points,y_val)

    def crv_intersection(self, x1_points,y1_points,x2_points,y2_points):
        """
 ========== description ============== 
Поиск пересечений для кривых заданных таблицами. Используется линейная интерполяция. Возможно несколько решений. 
        
 ==========  arguments  ============== 

     x1_points - таблица аргументов функции 1    

     y1_points - таблица значений функции 1  количество агрументов и значений функции должно совпадать  для табличной функции одному аргументу соответствует  строго одно значение ф..см.мануал   

     x2_points - таблица аргументов функции 2    

     y2_points - таблица значений функции 2  количество агрументов и значений функции должно совпадать  для табличной функции одному аргументу соответствует  строго одно значение ф..см.мануал  

        """

        self.f_crv_intersection = self.book.macro("crv_intersection")
        return self.f_crv_intersection(x1_points,y1_points,x2_points,y2_points)

    def crv_fit_spline_1D(self, xa,YA,m,XIA,WA,XCA,YCA,DCA,hermite=False):
        """
 ========== description ============== 
Поиск пересечений для кривых заданных таблицами. Используется линейная интерполяция. Возможно несколько решений. 
        
 ==========  arguments  ============== 

     xa - x значения исходных данных (строка значений или массив)    

     ya - y значения исходных данных (столбец значений или массив)  м - количество точек для сплайна интерполяции    

     должно быть четное для hermite = true    

     xia - таблица выходных значений  столбц значений (x) или массив. значения в возрастающем порядке  если не заданы возвращаются кубические коэффициента для каждого сегмента    

     wa - веса исходных данных    

     xca - х значения матрицы ограничений (столбец или массив)    

     yca - величина ограничения для заданного значения (столбец или массив)    

     dca - тип ограничения. 0 - значение, 1 - наклон. (столбец или массив).  если хоть одно из ограничений не задано - они не учитываются    

     должно быть четное для hermite = true  xia - таблица выходных значений  столбц значений (x) или массив. значения в возрастающем порядке  если не заданы возвращаются кубические..см.мануал  

        """

        self.f_crv_fit_spline_1D = self.book.macro("crv_fit_spline_1D")
        return self.f_crv_fit_spline_1D(xa,YA,m,XIA,WA,XCA,YCA,DCA,hermite)

    def crv_fit_linear(self, YA,xa,out,weight,constraints):
        """
 ========== description ============== 
Аппроксимация данных линейной функцией. Решается задача min|XM-Y| ищется вектор M 
        
 ==========  arguments  ============== 

     ya - y вектор исходных данных [0..n-1] (столбец или массив)    

     xa - x матрица исходных данных [0..n-1, 0..d-1] (таблица или массив)    

     out - тип вывода, out=0 (по умолчанию) коэффициенты аппроксимации [0..d-1],  out=1 код ошибки подбора аппроксимации  out=2 отчет по подбору аппроксимации, avgerror, avgrelerror..см.мануал   

     weight - вектор весов [0..n-1] для каждого параметра исходных данных    

     constraints - матрица ограничений с [0..k-1, 0..d] такая что  c[i,0]*m[0] + ... + c[i,d-1]*c[d-1] = cmatrix[i,d]   

        """

        self.f_crv_fit_linear = self.book.macro("crv_fit_linear")
        return self.f_crv_fit_linear(YA,xa,out,weight,raints)

    def crv_fit_poly(self, YA,xa,m,out,XIA,weight,constraints):
        """
 ========== description ============== 
Аппроксимация данных полиномом функцией. Решается задача min|XM-Y| ищется вектор M 
        
 ==========  arguments  ============== 

     ya - y вектор исходных данных [0..n-1] (столбец или массив)    

     xa - х вектор исходных данных [0..n-1] (таблица или массив)    

     m - степень полинома для аппроксимации    

     out - тип вывода, out=0 (по умолчанию) значения полинома для xia,  out=1 код ошибки аппроксимации  out=2 отчет по подбору аппроксимации, avgerror, avgrelerror, maxerror, rmserr..см.мануал   

     out - тип вывода, out=0 (по умолчанию) значения полинома для xia,  out=1 код ошибки аппроксимации  out=2 отчет по подбору аппроксимации, avgerror, avgrelerror, maxerror, rmserr..см.мануал   

     weight - вектор весов [0..n-1] для каждого параметра исходных данных    

     constraints - матрица ограничений с[0..k-1,0..2]. с[i,0] - значение x где задано ограничение  с[i,1] - велична ограничения, с[i,2] - тип ограничения (0 -значение,1 -производная)..см.мануал  

        """

        self.f_crv_fit_poly = self.book.macro("crv_fit_poly")
        return self.f_crv_fit_poly(YA,xa,m,out,XIA,weight,raints)

    def crv_parametric_interpolation(self, x_points,y_points,x_val,type_interpolation=0,param_points=-1):
        """
 ========== description ============== 
 интерполяция функции заданной параметрически (параметр номер значения) 
        
 ==========  arguments  ============== 

     x_points - таблица аргументов функции    

     y_points - таблица значений функции  количество агрументов и значений функции должно совпадать  для табличной функции одному аргументу соответствует  строго одно значение функ..см.мануал   

     x_val - аргумент для которого надо найти значение  одно значение в ячейке или диапазон значений  для диапазона аргументов будет найден диапазон значений  диапазоны могут быть ..см.мануал   

     type_interpolation - тип интерполяции  0 - линейная интерполяция  1 - кубическая интерполяция  2 - интерполяция акима (выбросы)  www.en.wikipedia.org/wiki/akima_spline  3 - ..см.мануал   

   param_points  

        """

        self.f_crv_parametric_interpolation = self.book.macro("crv_parametric_interpolation")
        return self.f_crv_parametric_interpolation(x_points,y_points,x_val,type_interpolation,param_points)

    def Ei(self, x):
        """
 ========== description ============== 
 Расчет интегральной показательной функции Ei(x) 
        
 ==========  arguments  ============== 

     x - агрумент функции, может быть и положительным и отрицательным   

        """

        self.f_Ei = self.book.macro("Ei")
        return self.f_Ei(x)

    def E_1(self, x):
        """
 ========== description ============== 
 Расчет интегральной показательной функции $E_1(x)$  для вещественных положительных x, x>0 верно E_1(x)=- Ei(-x) 
        
 ==========  arguments  ============== 

     x - агрумент функции, может быть и положительным и отрицательным   

        """

        self.f_E_1 = self.book.macro("E_1")
        return self.f_E_1(x)

    def transient_pd_radial(self, td,cd=0,skin=0,rd=1,model=0):
        """
 ========== description ============== 
 Расчет неустановившегося решения уравнения фильтрации  для различных моделей радиального притока к вертикльной скважине  основано не решениях в пространстве Лапласа и преобразовании Стефеста 
        
 ==========  arguments  ============== 

     td - безразмерное время для которого проводится расчет  сd - безразмерный коэффициент влияния ствола скважины    

   cd   

     skin - скин-фактор, безразмерный skin>0.  для skin<0 используйте эффективный радиус скважины    

     rd - безразмерное расстояние для которого проводится расчет  rd=1 соответвует забою скважины    

     model - модель проведения расчета. 0 - модель линейного стока ei  1 - модель линейного стока через преобразование стефеста  2 - конечный радиус скважины  3 - линейный сток со ..см.мануал  

        """

        self.f_transient_pd_radial = self.book.macro("transient_pd_radial")
        return self.f_transient_pd_radial(td,cd,skin,rd,model)

    def transient_pwf_radial_atma(self, t_day,qliq_sm3day,pi_atma=250,skin=0,cs_1atm=0,r_m=0.1,rw_m=0.1,k_mD=100,h_m=10,porosity=0.2,mu_cP=1,b_m3m3=1.2,ct_1atm=0.00001,model=0):
        """
 ========== description ============== 
 расчет изменения забойного давления после запуска скважины  с постоянным дебитом (terminal rate solution) 
        
 ==========  arguments  ============== 

     t_day - время для которого проводится расчет, сут    

     qliq_sm3day - дебит запуска скважины, м3/сут в стандартных условиях    

     pi_atma - начальное пластовое давление, атма    

     skin - скин - фактор, может быть отрицательным    

     cs_1atm - коэффициент влияния ствола скважины, 1/атм    

     r_m - расстояние от скважины для которого проводится расчет, м    

     rw_m - радиус скважины, м    

     k_md - проницаемость пласта, мд    

     h_m - толщина пласта, м    

     porosity - пористость    

     mu_cp - вязкость флюида в пласте, сп    

     b_m3m3 - объемный коэффициент нефти, м3/м3    

     ct_1atm - общая сжимаемость системы в пласте, 1/атм    

     model - модель проведения расчета. 0 - модель линейного стока ei  1 - модель линейного стока через преобразование стефеста  2 - конечный радиус скважины  3 - линейный сток со ..см.мануал  

        """

        self.f_transient_pwf_radial_atma = self.book.macro("transient_pwf_radial_atma")
        return self.f_transient_pwf_radial_atma(t_day,qliq_sm3day,pi_atma,skin,cs_1atm,r_m,rw_m,k_mD,h_m,porosity,mu_cP,b_m3m3,ct_1atm,model)

    def transient_def_cd(self, cs_1atm,rw_m=0.1,h_m=10,porosity=0.2,ct_1atm=0.00001):
        """
 ========== description ============== 
 расчет безразмерного коэффициента влияния ствола скважины (определение) 
        
 ==========  arguments  ============== 

     cs_1atm - коэффициент влияния ствола скважины, 1/атм    

     rw_m - радиус скважины, м    

     h_m - толщина пласта, м    

     porosity - пористость    

     ct_1atm - общая сжимаемость системы в пласте, 1/атм   

        """

        self.f_transient_def_cd = self.book.macro("transient_def_cd")
        return self.f_transient_def_cd(cs_1atm,rw_m,h_m,porosity,ct_1atm)

    def transient_def_cs_1atm(self, cd,rw_m=0.1,h_m=10,porosity=0.2,ct_1atm=0.00001):
        """
 ========== description ============== 
 расчет коэффициента влияния ствола скважины (определение) 
        
 ==========  arguments  ============== 

   cd   

     rw_m - радиус скважины, м    

     h_m - толщина пласта, м    

     porosity - пористость    

     ct_1atm - общая сжимаемость системы в пласте, 1/атм   

        """

        self.f_transient_def_cs_1atm = self.book.macro("transient_def_cs_1atm")
        return self.f_transient_def_cs_1atm(cd,rw_m,h_m,porosity,ct_1atm)

    def transient_def_td(self, t_day,rw_m=0.1,k_mD=100,porosity=0.2,mu_cP=1,ct_1atm=0.00001):
        """
 ========== description ============== 
 расчет безразмерного времени (определение) 
        
 ==========  arguments  ============== 

     t_day - время для которого проводится расчет, сут    

     rw_m - радиус скважины, м    

     k_md - проницаемость пласта, мд    

     porosity - пористость    

     mu_cp - вязкость флюида в пласте, сп    

     ct_1atm - общая сжимаемость системы в пласте, 1/атм   

        """

        self.f_transient_def_td = self.book.macro("transient_def_td")
        return self.f_transient_def_td(t_day,rw_m,k_mD,porosity,mu_cP,ct_1atm)

    def transient_def_t_day(self, td,rw_m=0.1,k_mD=100,porosity=0.2,mu_cP=1,ct_1atm=0.00001):
        """
 ========== description ============== 
 расчет времени по безразмерному времени (определение) 
        
 ==========  arguments  ============== 

   td   

     rw_m - радиус скважины, м    

     k_md - проницаемость пласта, мд    

     porosity - пористость    

     mu_cp - вязкость флюида в пласте, сп    

     ct_1atm - общая сжимаемость системы в пласте, 1/атм   

        """

        self.f_transient_def_t_day = self.book.macro("transient_def_t_day")
        return self.f_transient_def_t_day(td,rw_m,k_mD,porosity,mu_cP,ct_1atm)

    def transient_def_pd(self, Pwf_atma,qliq_sm3day,pi_atma=250,k_mD=100,h_m=10,mu_cP=1,b_m3m3=1.2):
        """
 ========== description ============== 
 расчет безразмерного давления (определение) 
        
 ==========  arguments  ============== 

     pwf_atma - забойное давление, атма    

     qliq_sm3day - дебит запуска скважины, м3/сут в стандартных условиях    

     pi_atma - начальное пластовое давление, атма    

     k_md - проницаемость пласта, мд    

     h_m - толщина пласта, м    

     mu_cp - вязкость флюида в пласте, сп    

     b_m3m3 - объемный коэффициент нефти, м3/м3   

        """

        self.f_transient_def_pd = self.book.macro("transient_def_pd")
        return self.f_transient_def_pd(Pwf_atma,qliq_sm3day,pi_atma,k_mD,h_m,mu_cP,b_m3m3)

    def transient_def_pwf_atma(self, pd,qliq_sm3day,pi_atma=250,k_mD=100,h_m=10,mu_cP=1,b_m3m3=1.2):
        """
 ========== description ============== 
 расчет безразмерного давления (определение) 
        
 ==========  arguments  ============== 

   pd   

     qliq_sm3day - дебит запуска скважины, м3/сут в стандартных условиях    

     pi_atma - начальное пластовое давление, атма    

     k_md - проницаемость пласта, мд    

     h_m - толщина пласта, м    

     mu_cp - вязкость флюида в пласте, сп    

     b_m3m3 - объемный коэффициент нефти, м3/м3   

        """

        self.f_transient_def_pwf_atma = self.book.macro("transient_def_pwf_atma")
        return self.f_transient_def_pwf_atma(pd,qliq_sm3day,pi_atma,k_mD,h_m,mu_cP,b_m3m3)

#UniflocVBA = API(addin_name_str)
