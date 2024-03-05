import os
import re
from PIL import Image, ImageDraw, ImageFont  

script_dir = os.path.dirname(os.path.abspath(__file__))

# flip horazonal
def flip_mug_image(image, sku): 
    if re.match(r"JMUG11WB[A-Z0-9]*|ACRTOPRCT[A-Z0-9]*", sku):  
        image = image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)  
    draw = ImageDraw.Draw(image)  
    return image, draw


# barcode  
IDAutomationHC39M_font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts', 'IDAutomationHC39M.ttf')  

def add_order_number_to_jmug(draw, sku, row, load_font):    
    if re.match(r"JMUG11WB[A-Z0-9]*", sku):    
        order_number = "*" + str(row['Order - Number']).strip('"') + "*"    
        font_size_order_number = 30 # font size    
        font_order_number = load_font(sku, IDAutomationHC39M_font_path, font_size_order_number)    
        processed_font_color = (0, 0, 0)  # font color (black)    
        draw.text((100, 790), order_number, fill=processed_font_color, font=font_order_number)  # position

sku_to_image = { 

    # customizable
    "JMUG11WBUVPPSLNTBBUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPPSICG1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),    
    "JMUG11WBUVPPSNNCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMSAYOCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPJMSAYOCMUVP.png'),
    "JMUG11WBUVPPSWIPEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSWIPEUVP.png'),
    "JMUG11WBUVPPSMUWRMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSMUWRMUVP.png'),
    "JMUG11WBUVPJMBTOIMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPJMBTOIMUVP.png'),
    "JMUG11WBSUBJMSUWOMSUB": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'SUBJMSUWOMSUB.png'),
    "JMUG11WBUVPPSSPERMMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSSPERMMUVP.png'),
    "JMUG11WBUVPPSBONDUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSBONDUVP.png'),
    "JMUG11WBSUBUYTHTSUB": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'SUBUYTHTSUB.png'),
    "JMUG11WBUVPJMFMEMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPJMFMEMUVP.png'),
    "JMUG11WBUVPPSYBCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSYBCMUVP.png'),
    "JMUG11WBUVPPSSBFRUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSSBFRUVP.png'),
    "JMUG11WBUVPJMCCAS1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCAS2UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCAS3UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCTNR1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCTNR2UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCTNR3UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCDS1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCDS2UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPJMCCDS3UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPPSBALLS2UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSBALLS2UVP.png'),
    "JMUG11WBUVPCCFREKEX1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPCCFREKEX1UVP.png'),
    "JMUG11WBUVPPSTYBMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSTYBMUVP.png'),
    "JMUG11WBUVPPSSBNALUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'blank_.png'),
    "JMUG11WBUVPPSPFCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSPFCMUVP.png'),
    "JMUG11WBUVPPSLAYBNSMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSLAYBNSMUVP.png'),

    # fav child
    "JMUG11WBUVPPSFAVCHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSFAVCHUVP.png'),
    "JMUG11WBUVPPS2FAVCHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPS2FAVCHUVP.png'),
    "JMUG11WBUVPPS3FAVCHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPS3FAVCHUVP.png'),
    "JMUG11WBUVPPS4FAVCHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPS4FAVCHUVP.png'),

    # christmas
    "JMUG11WBUVPPSCMSMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSCMSMUVP.png'),
    "JMUG11WBUVPPSCMSRUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSCMSRUVP.png'),
    "JMUG11WBUVPPSCMGRUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSCMGRUVP.png'),
    "JMUG11WBUVPCCKHCSMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPCCKHCSMUVP.png'),

    # Little Miss
    "JMUG11WBUVPPSLILMSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable', 'UVPPSLILMSUVP.png'),
    "JMUG11WBUVPPSLILMGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable','UVPPSLILMGUVP.png'),
    "JMUG11WBUVPPSLILMPUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'customizable','UVPPSLILMPUVP.png'),
    
    # stable
    "JMUG11WBUVPCAITSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPCAITSUVP.png'),
    "JMUG11WBUVPCCBESTTMNUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPCCBESTTMNUVP.png'),
    "JMUG11WBUVPCCCRYPUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPCCCRYPUVP.png'),
    "JMUG11WBUVPCCSCHITTMUGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPCCSCHITTMUGUVP.png'),
    "JMUG11WBUVPCCUPMILFUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPCCUPMILFUVP.png'),
    "JMUG11WBUVPCCWEDCUPUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPCCWEDCUPUVP.png'),
    "JMUG11WBUVPCCWITCHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPCCWITCHUVP.png'),
    "JMUG11WBUVPDHDED2ME1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPDHDED2ME1UVP.png'),   
    "JMUG11WBUVPHIKEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPHIKEUVP.png'),
    "JMUG11WBUVPHOCUSMUGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPHOCUSMUGUVP.png'),
    "JMUG11WBUVPJMBFNEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMBFNEUVP.png'),
    "JMUG11WBUVPJMDCCUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMDCCUVP.png'),
    "JMUG11WBUVPJMDIRMEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMDIRMEUVP.png'),  
    "JMUG11WBUVPJMDLSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPJMDLSUVP.png'),
    "JMUG11WBUVPJMDWMMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMDWMMUVP.png'),
    "JMUG11WBUVPJMIHTDMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMIHTDMUVP.png'),
    "JMUG11WBUVPJMPCCUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPJMPCCUVP.png'),
    "JMUG11WBUVPJMSAWTUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMSAWTUVP.png'),
    "JMUG11WBUVPMONKEYSCCUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPMONKEYSCCUVP.png'),
    "JMUG11WBUVPPPSJEFFDMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPPSJEFFDMUVP.png'),
    "JMUG11WBUVPPSADHOUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSADHOUVP.png'),
    "JMUG11WBUVPPSASTRMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSASTRMUVP.png'),
    "JMUG11WBUVPPSBFCEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSBFCEUVP.png'),
    "JMUG11WBUVPPSBFNDMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSBFNDMUVP.png'),   
    "JMUG11WBUVPPSBFWOUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSBFWOUVP.png'),
    "JMUG11WBUVPPSROMEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSROMEUVP.png'),
    "JMUG11WBUVPPSCATMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSCATMUVP.png'),
    "JMUG11WBUVPPSCHIROUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSCHIROUVP.png'),
    "JMUG11WBUVPPSCUMUFUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSCUMUFUVP.png'),
    "JMUG11WBUVPPSDADABMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSDADABMUVP.png'),
    "JMUG11WBUVPPSDFCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSDFCMUVP.png'),
    "JMUG11WBUVPPSDJLOUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSDJLOUVP.png'),
    "JMUG11WBUVPPSDMDWUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSDMDWUVP.png'),
    "JMUG11WBUVPPSDOCAUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSDOCAUVP.png'),
    "JMUG11WBUVPPSDTCNUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSDTCNUVP.png'),
    "JMUG11WBUVPPSDUMBUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSDUMBUVP.png'),
    "JMUG11WBUVPPSEPTUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSEPTUVP.png'),
    "JMUG11WBUVPPSFQOHRUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSFQOHRUVP.png'),
    "JMUG11WBUVPPSHUDBCUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSHUDBCUVP.png'),
    "JMUG11WBUVPPSHUDICKUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSHUDICKUVP.png'),
    "JMUG11WBUVPPSIBGMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSIBGMUVP.png'),
    "JMUG11WBUVPPSIDRBHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSIDRBHUVP.png'),
    "JMUG11WBUVPDHDED2ME1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPDHDED2ME1UVP.png'),   
    "JMUG11WBUVPHIKEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPHIKEUVP.png'),
    "JMUG11WBUVPHOCUSMUGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPHOCUSMUGUVP.png'),
    "JMUG11WBUVPPSIGBBJSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSIGBBJSUVP.png'),
    "JMUG11WBUVPPSINAMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSINAMUVP.png'),
    "JMUG11WBUVPPSJBANHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSJBANHUVP.png'),
    "JMUG11WBUVPPSJCM1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSJCM1UVP.png'),
    "JMUG11WBUVPPSJOEBGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSJOEBGUVP.png'),  
    "JMUG11WBUVPPSKIMJMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSKIMJMUVP.png'),
    "JMUG11WBUVPPSLALPUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSLALPUVP.png'),
    "JMUG11WBUVPPSLAYGASMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSLAYGASMUVP.png'),
    "JMUG11WBUVPUVPPSLVSBUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSLVSBUVP.png'),
    "JMUG11WBUVPPSMACASSMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSMACASSMUVP.png'),
    "JMUG11WBUVPPSMMMBMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSMMMBMUVP.png'),
    "JMUG11WBUVPPSMOMBAUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSMOMBAUVP.png'),
    "JMUG11WBUVPPSNBAHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSNBAHUVP.png'),
    "JMUG11WBUVPPSNCATUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSNCATUVP.png'),   
    "JMUG11WBUVPPSOKILUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSOKILUVP.png'), 
    "JMUG11WBUVPPSONEDEGREEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSONEDEGREEUVP.png'),
    "JMUG11WBUVPPSOWACUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSOWACUVP.png'),
    "JMUG11WBUVPPSPFDKUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSPFDKUVP.png'),
    "JMUG11WBUVPPSPPLYUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSPPLYUVP.png'),
    "JMUG11WBUVPPSPRSWDLUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSPRSWDLUVP.png'),
    "JMUG11WBUVPPSPRSWDMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSPRSWDMUVP.png'),
    "JMUG11WBUVPPSRTTTSMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSRTTTSMUVP.png'),
    "JMUG11WBUVPPSSHITTERSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSSHITTERSUVP.png'),
    "JMUG11WBUVPPSSLPCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSSLPCMUVP.png'),
    "JMUG11WBUVPPSSMUGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSSMUGUVP.png'),
    "JMUG11WBUVPPSSTFUUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSSTFUUVP.png'),
    "JMUG11WBUVPPSSWALLOWUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSSWALLOWUVP.png'),
    "JMUG11WBUVPPSTDLCMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSTDLCMUVP.png'),
    "JMUG11WBUVPPSTHMDCUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSTHMDCUVP.png'),
    "JMUG11WBUVPPSTOB1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSTOB1UVP.png'),
    "JMUG11WBUVPPSTOD1UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSTOD1UVP.png'),
    "JMUG11WBUVPPSTOPBMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSTOPBMUVP.png'),
    "JMUG11WBUVPPSTWAFUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSTWAFUVP.png'),   
    "JMUG11WBUVPPSUHOHUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSUHOHUVP.png'),
    "JMUG11WBUVPPSVAGMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSVAGMUVP.png'),   
    "JMUG11WBUVPPSWGFMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSWGFMUVP.png'),   
    "JMUG11WBUVPPSYFACMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPPSYFACMUVP.png'),
    "JMUG11WBUVPPSYINAPUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSYINAPUVP.png'),
    "JMUG11WBUVPRACAIMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPRACAIMUVP.png'),
    "JMUG11WBUVPRAPMAGUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPRAPMAGUVP.png'),
    "JMUG11WBUVPRATODPUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPRATODPUVP.png'),
    "JMUG11WBUVPRMCMDND5UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPRMCMDND5UVP.png'),
    "JMUG11WBUVPRMCMDND6UVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPRMCMDND6UVP.png'),
    "JMUG11WBUVPROFSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPROFSUVP.png'),
    "JMUG11WBUVPttsmmuUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPttsmmuUVP.png'),
    "JMUG11WBUVPPSSWTUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSSWTUVP.png'),
    "JMUG11WBSUBBOSSUB": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'SUBBOSSUB.png'),
    "JMUG11WBUVPJMBFMEUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable','UVPJMBFMEUVP.png'),
    "JMUG11WBUVPPSNCATUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSNCATUVP.png'),
    "JMUG11WBUVPPSOFFSUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSOFFSUVP.png'),
    "JMUG11WBUVPPSPFDKUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSPFDKUVP.png'),
    "JMUG11WBUVPJMSHITTERUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPJMSHITTERUVP.png'),
    "JMUG11WBUVPPSINAMUVP": os.path.join(os.path.dirname(os.path.realpath(__file__)), 'background', 'mugs', 'stable', 'UVPPSINAMUVP.png'),
}

sku_to_font = {

    # customizable
    'JMUG11WBUVPPSLNTBBUVP': os.path.join(script_dir, 'fonts', 'TeXGyre-Termes-Bold.ttf'),
    'JMUG11WBUVPPSICG1UVP': os.path.join(script_dir, 'fonts', 'TeXGyre-Termes-Bold.ttf'),
    'JMUG11WBUVPPSNNCMUVP': os.path.join(script_dir, 'Fonts', 'LibreBaskerville.ttf'),
    'JMUG11WBUVPJMSAYOCMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSWIPEUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSMUWRMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPJMBTOIMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBSUBJMSUWOMSUB': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSSPERMMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'), 
    'JMUG11WBUVPPSBONDUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBSUBUYTHTSUB': os.path.join(script_dir, 'fonts', 'Shorelines Script Bold.ttf'),
    'JMUG11WBUVPJMFMEMUVP': os.path.join(script_dir, 'fonts', 'I Love Glitter.ttf'),
    'JMUG11WBUVPPSYBCMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSSBFRUVP': os.path.join(script_dir, 'fonts', 'Gabriel_Weiss_Friends.ttf'),
    'JMUG11WBUVPJMCCAS1UVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPJMCCAS2UVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPJMCCAS3UVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPJMCCTNR1UVP': os.path.join(script_dir, 'fonts', 'Times New Roman-Regular.ttf'),
    'JMUG11WBUVPJMCCTNR2UVP': os.path.join(script_dir, 'fonts', 'Times New Roman-Regular.ttf'),
    'JMUG11WBUVPJMCCTNR3UVP': os.path.join(script_dir, 'fonts', 'Times New Roman-Regular.ttf'),
    'JMUG11WBUVPJMCCDS1UVP': os.path.join(script_dir, 'fonts', 'DancingScript-Bold.ttf'),
    'JMUG11WBUVPJMCCDS2UVP': os.path.join(script_dir, 'fonts', 'DancingScript-Bold.ttf'),
    'JMUG11WBUVPJMCCDS3UVP': os.path.join(script_dir, 'fonts', 'DancingScript-Bold.ttf'),
    'JMUG11WBUVPPSBALLS2UVP': os.path.join(script_dir, 'fonts', 'Louis George Cafe.ttf'),
    'JMUG11WBUVPCCFREKEX1UVP': os.path.join(script_dir, 'fonts', 'Shorelines Script Bold.ttf'),
    'JMUG11WBUVPPSTYBMUVP': os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),
    'JMUG11WBUVPPSSBNALUVP': os.path.join(script_dir, 'fonts', 'TeXGyre-Termes-Bold.ttf'),
    'JMUG11WBUVPPSPFCMUVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),
    'JMUG11WBUVPPSLAYBNSMUVP': os.path.join(script_dir, 'fonts', 'Brittney.ttf'),
    
    # fav child
    "JMUG11WBUVPPSFAVCHUVP": os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),
    "JMUG11WBUVPPS2FAVCHUVP": os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),
    "JMUG11WBUVPPS3FAVCHUVP": os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),
    "JMUG11WBUVPPS4FAVCHUVP": os.path.join(script_dir, 'fonts', 'AmaticSC-Regular.ttf'),

    
    # christmas
    'JMUG11WBUVPPSCMSMUVP': os.path.join(script_dir, 'fonts', 'Farmer Market Regular.ttf'),
    'JMUG11WBUVPPSCMSRUVP': os.path.join(script_dir, 'fonts', 'Farmer Market Regular.ttf'),
    'JMUG11WBUVPPSCMGRUVP': os.path.join(script_dir, 'fonts', 'Farmer Market Regular.ttf'),
    'JMUG11WBUVPCCKHCSMUVP': os.path.join(script_dir, 'fonts', 'Blueberry.ttf'),

    # Little Miss
    "JMUG11WBUVPPSLILMSUVP": os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),
    "JMUG11WBUVPPSLILMGUVP": os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),
    "JMUG11WBUVPPSLILMPUVP": os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),

}

sku_to_second_line_font = { 

    # customizable
    'JMUG11WBUVPPSLNTBBUVP': os.path.join(script_dir, 'fonts', 'Brittney.ttf'),
    'JMUG11WBUVPPSICG1UVP': os.path.join(script_dir, 'fonts', 'AmaticSC-Bold.ttf'),
    'JMUG11WBUVPPSNNCMUVP': os.path.join(script_dir, 'fonts', 'Brittney.ttf'),
    'JMUG11WBUVPPSTYBMUVP': os.path.join(script_dir, 'fonts', 'BebasNeue-Regular.ttf'),
    'JMUG11WBUVPPSSBNALUVP': os.path.join(script_dir, 'fonts', 'Brittney.ttf'),
}

sku_to_third_line_font = { 

    # customizable
    'JMUG11WBUVPPSNNCMUVP': os.path.join(script_dir, 'fonts', 'LibreBaskerville.ttf'),
    
}

sku_to_fontsize_placement = {  # (font-size, x, y)  

    # customizable
    'JMUG11WBUVPPSLNTBBUVP': {     
         1: (600, 50),
    },
    'JMUG11WBUVPPSICG1UVP': {     
         1: (600, 50),
    },
    'JMUG11WBUVPPSNNCMUVP': {     
         1: (500, 0),
    },
    'JMUG11WBUVPJMSAYOCMUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPPSWIPEUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPPSMUWRMUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPJMBTOIMUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBSUBJMSUWOMSUB': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPPSSPERMMUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBUVPPSBONDUVP': {     
         1: (90, 330, 590),  2: (90, 330, 590), 3: (90, 330, 590),  4: (90, 330, 590),  5: (90, 330, 590),  
         6: (90, 330, 590),  7: (90, 330, 590),  8: (90, 330, 590),  9: (90, 330, 590), 10: (80, 330, 590),  
        11: (80, 330, 590), 12: (80, 330, 590), 13: (80, 330, 590), 14: (60, 330, 580), 15: (60, 330, 580), 
        16: (60, 330, 580), 17: (60, 330, 580), 18: (40, 330, 570), 19: (40, 330, 570), 20: (40, 330, 570),
    },
    'JMUG11WBSUBUYTHTSUB': {     
         1: (60, 520),  2: (60, 520),  3: (60, 520),  4: (60, 520),  5: (60, 520),  
         6: (60, 520),  7: (60, 520),  8: (60, 520),  9: (60, 520), 10: (60, 520),  
        11: (60, 520), 12: (60, 520), 13: (60, 520), 14: (50, 530), 15: (50, 530), 
        16: (50, 530), 17: (50, 530), 18: (50, 530), 19: (40, 540), 20: (40, 540),
    },
    'JMUG11WBUVPJMFMEMUVP': {     
         1: (100, 200, 570),  2: (100, 200, 570),  3: (100, 200, 570),  4: (100, 200, 570),  5: (100, 200, 570),  
         6: (100, 150, 570),  7: (100, 150, 570),  8: (100, 150, 570),  9: (100, 150, 570), 10: (100, 150, 570),  
        11: (100, 100, 570), 12: (100, 100, 570), 13: (100, 100, 570), 14: (90, 100, 580), 15: (90, 100, 580), 
        16: (90, 50, 580), 17: (90, 50, 580), 18: (90, 50, 580), 19: (80, 50, 590), 20: (80, 50, 590),
    },
    'JMUG11WBUVPPSYBCMUVP': {     
         1: (180, 480),  2: (180, 480),  3: (180, 480),  4: (180, 480),  5: (180, 480),  
         6: (180, 480),  7: (180, 480),  8: (150, 500),  9: (150, 500), 10: (150, 500),  
        11: (130, 520), 12: (130, 520), 13: (130, 520), 14: (100, 530), 15: (100, 530), 
        16: (100, 530), 17: (90, 530),  18: (90, 530),  19: (80, 530),  20: (80, 530),
        21: (70, 530),  22: (70, 530),  23: (70, 530),  24: (60, 540),  25: (60, 540),
    },
    'JMUG11WBUVPPSSBFRUVP': {     
         1: (85, 330),  2: (85, 330),  3: (85, 330),  4: (85, 330),  5: (85, 330),  
         6: (85, 330),  7: (85, 330),  8: (85, 330),  9: (85, 330), 10: (85, 330),  
        11: (85, 330), 12: (85, 330), 13: (85, 330), 14: (85, 330), 15: (85, 330), 
        16: (70, 340), 17: (70, 340), 18: (70, 340), 19: (70, 340), 20: (70, 340),
        21: (60, 350), 22: (60, 350), 23: (60, 350), 24: (50, 360), 25: (50, 360),
    },
    'JMUG11WBUVPJMCCAS1UVP': {   
         1: (150, 250),   2: (150, 250),   3: (150, 250),   4: (150, 250),   5: (150, 250),  
         6: (150, 250),   7: (150, 250),   8: (150, 250),   9: (130, 260),  10: (130, 260),       
        11: (130, 260), 12: (130, 260), 13: (110, 270), 14: (110, 270), 15: (110, 270), 
        16: (110, 270), 17: (100, 270), 18: (100, 270), 19: (100, 270), 20: (100, 270),
        21: (80, 280), 22: (80, 280), 23: (80, 280), 24: (80, 280), 25: (80, 280), 
        26: (70, 280), 27: (70, 280), 28: (60, 280), 29: (55, 280), 30: (50, 280), 
        31: (50, 280), 32: (40, 290), 33: (40, 290), 34: (30, 290), 35: (30, 290),
    },
    'JMUG11WBUVPJMCCAS2UVP': {     
         1: (150, 150),  2: (150, 150),  3: (150, 150),  4: (150, 150),  5: (150, 150),  
         6: (150, 150),  7: (150, 150),  8: (150, 150),  9: (130, 160), 10: (130, 160),       
        11: (130, 160), 12: (130, 160), 13: (110, 170), 14: (110, 170), 15: (110, 170), 
        16: (110, 170), 17: (100, 170), 18: (100, 170), 19: (100, 170), 20: (100, 170),
        21: (80, 180),  22: (80, 180), 23: (80, 180),   24: (80, 180),  25: (80, 180), 
        26: (70, 180),  27: (70, 180), 28: (60, 180),   29: (55, 180),  30: (50, 180), 
        31: (50, 180),  32: (40, 190), 33: (40, 190),   34: (30, 190),  35: (30, 190),
    },
    'JMUG11WBUVPJMCCAS3UVP': {     
         1: (150, 50),   2: (150, 50),   3: (150, 50),   4: (150, 50),   5: (150, 50),  
         6: (150, 50),   7: (150, 50),   8: (150, 50),   9: (130, 60),  10: (130, 60),       
        11: (130, 60), 12: (130, 60), 13: (110, 70), 14: (110, 70), 15: (110, 70), 
        16: (110, 70), 17: (100, 70), 18: (100, 70), 19: (100, 70), 20: (100, 70),
        21: (80, 80), 22: (80, 80), 23: (80, 80), 24: (80, 80), 25: (80, 80), 
        26: (70, 80), 27: (70, 80), 28: (60, 80), 29: (55, 80), 30: (50, 80), 
        31: (50, 80), 32: (40, 90), 33: (40, 90), 34: (30, 90), 35: (30, 90),
    },
    'JMUG11WBUVPJMCCTNR1UVP': {
         1: (150, 250),   2: (150, 250),   3: (150, 250),   4: (150, 250),   5: (150, 250),  
         6: (150, 250),   7: (140, 255),   8: (140, 255),   9: (130, 260),  10: (130, 260),       
        11: (120, 260), 12: (110, 260), 13: (100, 270), 14: (100, 270), 15: (90, 270), 
        16: (80, 280), 17: (80, 280), 18: (70, 285), 19: (70, 285), 20: (60, 290),
        21: (60, 290), 22: (60, 290), 23: (50, 295), 24: (50, 295), 25: (50, 295), 
        26: (50, 295), 27: (50, 295), 28: (40, 300), 29: (40, 300), 30: (40, 300), 
        31: (40, 300), 32: (40, 300), 33: (40, 300), 34: (40, 300), 35: (40, 300),
    },
    'JMUG11WBUVPJMCCDS1UVP': { 
         1: (150, 250),   2: (150, 250),   3: (150, 250),   4: (150, 250),   5: (150, 250),  
         6: (150, 250),   7: (140, 255),   8: (140, 255),   9: (130, 260),  10: (130, 260),       
        11: (120, 260), 12: (110, 260), 13: (100, 270), 14: (100, 270), 15: (90, 270), 
        16: (80, 280), 17: (80, 280), 18: (70, 285), 19: (70, 285), 20: (60, 290),
        21: (60, 290), 22: (60, 290), 23: (50, 295), 24: (50, 295), 25: (50, 295), 
        26: (50, 295), 27: (50, 295), 28: (40, 300), 29: (40, 300), 30: (40, 300), 
        31: (40, 300), 32: (40, 300), 33: (40, 300), 34: (40, 300), 35: (40, 300),
    },
    'JMUG11WBUVPJMCCTNR2UVP': {     
         1: (150, 150),   2: (150, 150),   3: (150, 150),   4: (150, 150),   5: (150, 150),  
         6: (150, 150),   7: (150, 150),   8: (150, 150),   9: (130, 160),  10: (130, 160),       
        11: (130, 160), 12: (130, 160), 13: (110, 170), 14: (110, 170), 15: (110, 170), 
        16: (110, 170), 17: (100, 170), 18: (100, 170), 19: (100, 170), 20: (100, 170),
        21: (80, 180), 22: (80, 180), 23: (80, 180), 24: (80, 180), 25: (80, 180), 
        26: (70, 180), 27: (70, 180), 28: (60, 180), 29: (55, 180), 30: (50, 180), 
        31: (50, 180), 32: (40, 190), 33: (40, 190), 34: (30, 190), 35: (30, 190),
    },
    'JMUG11WBUVPJMCCTNR3UVP': {
         1: (150, 50),   2: (150, 50),   3: (150, 50),   4: (150, 50),   5: (150, 50),  
         6: (150, 50),   7: (150, 50),   8: (150, 50),   9: (130, 60),  10: (130, 60),       
        11: (130, 60), 12: (130, 60), 13: (110, 70), 14: (110, 70), 15: (110, 70), 
        16: (110, 70), 17: (100, 70), 18: (100, 70), 19: (100, 70), 20: (100, 70),
        21: (80, 80), 22: (80, 80), 23: (80, 80), 24: (80, 80), 25: (80, 80), 
        26: (70, 80), 27: (70, 80), 28: (60, 80), 29: (55, 80), 30: (50, 80), 
        31: (50, 80), 32: (40, 90), 33: (40, 90), 34: (30, 90), 35: (30, 90),
    },
    'JMUG11WBUVPJMCCDS1UVP': { 
         1: (150, 250),   2: (150, 250),   3: (150, 250),   4: (150, 250),   5: (150, 250),  
         6: (150, 250),   7: (140, 255),   8: (140, 255),   9: (130, 260),  10: (130, 260),       
        11: (120, 260), 12: (110, 260), 13: (100, 270), 14: (100, 270), 15: (90, 270), 
        16: (80, 280), 17: (80, 280), 18: (70, 285), 19: (70, 285), 20: (60, 290),
        21: (60, 290), 22: (60, 290), 23: (50, 295), 24: (50, 295), 25: (50, 295), 
        26: (50, 295), 27: (50, 295), 28: (40, 300), 29: (40, 300), 30: (40, 300), 
        31: (40, 300), 32: (40, 300), 33: (40, 300), 34: (40, 300), 35: (40, 300),
    },
    'JMUG11WBUVPJMCCDS2UVP': {     
         1: (150, 150),   2: (150, 150),   3: (150, 150),   4: (150, 150),   5: (150, 150),  
         6: (150, 150),   7: (150, 150),   8: (150, 150),   9: (130, 160),  10: (130, 160),       
        11: (130, 160), 12: (130, 160), 13: (110, 170), 14: (110, 170), 15: (110, 170), 
        16: (110, 170), 17: (100, 170), 18: (100, 170), 19: (100, 170), 20: (100, 170),
        21: (80, 180), 22: (80, 180), 23: (80, 180), 24: (80, 180), 25: (80, 180), 
        26: (70, 180), 27: (70, 180), 28: (60, 180), 29: (55, 180), 30: (50, 180), 
        31: (50, 180), 32: (40, 190), 33: (40, 190), 34: (30, 190), 35: (30, 190),
    },
    'JMUG11WBUVPJMCCDS3UVP': {
         1: (150, 50),   2: (150, 50),   3: (150, 50),   4: (150, 50),   5: (150, 50),  
         6: (150, 50),   7: (150, 50),   8: (150, 50),   9: (130, 60),  10: (130, 60),       
        11: (130, 60), 12: (130, 60), 13: (110, 70), 14: (110, 70), 15: (110, 70), 
        16: (110, 70), 17: (100, 70), 18: (100, 70), 19: (100, 70), 20: (100, 70),
        21: (80, 80), 22: (80, 80), 23: (80, 80), 24: (80, 80), 25: (80, 80), 
        26: (70, 80), 27: (70, 80), 28: (60, 80), 29: (55, 80), 30: (50, 80), 
        31: (50, 80), 32: (40, 90), 33: (40, 90), 34: (30, 90), 35: (30, 90),
    },
    'JMUG11WBUVPPSBALLS2UVP': {     
         1: (70, 600),  2: (70, 600),  3: (70, 600),  4: (70, 600),  5: (70, 600),  
         6: (70, 600),  7: (70, 600),  8: (70, 600),  9: (70, 600), 10: (70, 600),  
        11: (70, 600), 12: (70, 600), 13: (70, 600), 14: (70, 600), 15: (70, 600), 
        16: (55, 610), 17: (55, 610), 18: (55, 610), 19: (55, 610), 20: (55, 610),
        21: (45, 620), 22: (45, 620), 23: (45, 620), 24: (35, 630), 25: (35, 630),
    },
    'JMUG11WBUVPCCFREKEX1UVP': {     
         1: (60, 550),  2: (60, 550),  3: (60, 550),  4: (80, 550),  5: (60, 550),  
         6: (60, 550),  7: (60, 550),  8: (60, 550),  9: (60, 550), 10: (60, 550),  
        11: (60, 550), 12: (60, 550), 13: (60, 550), 14: (50, 560), 15: (50, 560), 
        16: (50, 560), 17: (50, 560), 18: (50, 560), 19: (40, 570), 20: (40, 570),
    },
    'JMUG11WBUVPPSTYBMUVP': {     
         1: (50, 300, 320),  2: (50, 300, 320),  3: (50, 300, 320),  4: (50, 300, 320),  5: (50, 300, 320),  
         6: (50, 300, 320),  7: (40, 300, 320),  8: (40, 300, 320),  9: (30, 300, 330), 10: (30, 300, 320),  
        11: (25, 300, 330), 12: (25, 300, 330), 13: (25, 300, 330), 14: (20, 300, 335), 15: (20, 300, 325), 
    },
    'JMUG11WBUVPPSSBNALUVP': {     
         1: (400, 50),
    },
    'JMUG11WBUVPPSPFCMUVP': {     
         1: (90, 610),  2: (90, 610), 3: (90, 610),  4: (90, 610),  5: (90, 610),  
         6: (90, 610),  7: (90, 610),  8: (90, 610),  9: (90, 610), 10: (80, 610),  
        11: (80, 610), 12: (80, 610), 13: (80, 610), 14: (60, 600), 15: (60, 600), 
        16: (60, 600), 17: (60, 600), 18: (40, 600), 19: (60, 600), 20: (60, 600),
        21: (40, 600), 22: (40, 600), 23: (40, 600), 24: (40, 600), 25: (40, 600),
    },
    'JMUG11WBUVPPSLAYBNSMUVP': {     
         1: (110, 550),  2: (110, 550), 3: (110, 550),  4: (110, 550),  5: (110, 550),  
         6: (110, 550),  7: (110, 550),  8: (110, 550),  9: (110, 550), 10: (110, 550),  
        11: (110, 550), 12: (110, 550), 13: (90, 550), 14: (90, 560), 15: (90, 560), 
        16: (90, 560), 17: (90, 560), 18: (90, 560), 19: (90, 560), 20: (70, 560),
        21: (70, 560), 22: (70, 560), 23: (70, 560), 24: (60, 560), 25: (60, 560),
    },

    
    # fav child
    'JMUG11WBUVPPSFAVCHUVP': {     
         1: (175, 110),  2: (175, 110),  3: (175, 110),  4: (175, 110),  5: (175, 110),  
         6: (175, 110),  7: (175, 110),  8: (175, 110),  9: (175, 110), 10: (155, 120),  
        11: (155, 120), 12: (125, 140), 13: (125, 140), 14: (100, 150), 15: (100, 150), 
    },
    'JMUG11WBUVPPS2FAVCHUVP': {     
         1: (135, 90),  2: (135, 90), 3: (135, 90), 4: (135, 90),  5: (135, 90),  
         6: (135, 90),  7: (135, 90), 8: (135, 90), 9: (135, 90), 10: (120, 100),  
        11: (120, 100), 12: (120, 100), 13: (90, 120), 14: (80, 130),  15: (80, 130), 
    },
    'JMUG11WBUVPPS3FAVCHUVP': {     
         1: (110, 110),  2: (110, 110),  3: (110, 110),  4: (110, 110),  5: (110, 110),  
         6: (110, 110),  7: (110, 110),  8: (110, 110),  9: (110, 110), 10: (110, 110),  
        11: (100, 110), 12: (100, 110), 13: (100, 110), 14: (100, 110), 15: (100, 110), 
    },
    'JMUG11WBUVPPS4FAVCHUVP': {     
         1: (100, 80), 2: (100, 80), 3: (100, 80), 4: (100, 80),  5: (100, 80),  
         6: (100, 80), 7: (100, 80), 8: (100, 80), 9: (100, 80), 10: (100, 80),  
        11: (90, 80), 12: (90, 80), 13: (90, 80), 14: (80, 85),  15: (80, 85), 
    },


    # christmas
    'JMUG11WBUVPPSCMSMUVP': {     
         1: (150, 540),  2: (150, 540),  3: (150, 540),  4: (150, 540),  5: (150, 540),  
         6: (150, 540),  7: (150, 540),  8: (150, 540),  9: (150, 540), 10: (150, 540),  
        11: (150, 540), 12: (130, 540), 13: (130, 540), 14: (110, 540), 15: (110, 540), 
        16: (90, 560),  17: (90, 560),  18: (90, 560),  19: (80, 560),  20: (80, 560),
    },
    'JMUG11WBUVPPSCMSRUVP': {     
         1: (150, 540),  2: (150, 540),  3: (150, 540),  4: (150, 540),  5: (150, 540),  
         6: (150, 540),  7: (150, 540),  8: (150, 540),  9: (150, 540), 10: (150, 540),  
        11: (150, 540), 12: (130, 540), 13: (130, 540), 14: (110, 540), 15: (110, 540), 
        16: (90, 560),  17: (90, 560),  18: (90, 560),  19: (80, 560),  20: (80, 560),
    },
    'JMUG11WBUVPPSCMGRUVP': {     
         1: (150, 540),  2: (150, 540),  3: (150, 540),  4: (150, 540),  5: (150, 540),  
         6: (150, 540),  7: (150, 540),  8: (150, 540),  9: (150, 540), 10: (150, 540),  
        11: (150, 540), 12: (130, 540), 13: (130, 540), 14: (110, 540), 15: (110, 540), 
        16: (90, 560),  17: (90, 560),  18: (90, 560),  19: (80, 560),  20: (80, 560),
    },
    'JMUG11WBUVPCCKHCSMUVP': {     
         1: (130, 500),  2: (130, 500),  3: (130, 500),  4: (130, 500),  5: (130, 500),  
         6: (130, 500),  7: (130, 500),  8: (130, 500),  9: (130, 500), 10: (130, 500),  
        11: (130, 500), 12: (110, 500), 13: (110, 500), 14: (90, 500), 15: (90, 500), 
        16: (70, 520),  17: (70, 520),  18: (70, 520),  19: (60, 520),  20: (60, 520),
    },

    # Little Miss
    'JMUG11WBUVPPSLILMGUVP': {     
         1: (130, 200),  2: (130, 200),  3: (130, 200),  4: (130, 200),  5: (130, 200),  
         6: (130, 200),  7: (130, 200),  8: (130, 200),  9: (130, 200), 10: (130, 200),  
        11: (130, 200), 12: (110, 200), 13: (110, 200), 14: (90, 200), 15: (90, 200), 
        16: (70, 220),  17: (70, 220),  18: (70, 220),  19: (60, 220),  20: (60, 220),
    },
    'JMUG11WBUVPPSLILMPUVP': {     
         1: (130, 200),  2: (130, 200),  3: (130, 200),  4: (130, 200),  5: (130, 200),  
         6: (130, 200),  7: (130, 200),  8: (130, 200),  9: (130, 200), 10: (130, 200),  
        11: (130, 200), 12: (110, 200), 13: (110, 200), 14: (90, 200), 15: (90, 200), 
        16: (70, 220),  17: (70, 220),  18: (70, 220),  19: (60, 220),  20: (60, 220),
    },
    'JMUG11WBUVPPSLILMSUVP': {     
         1: (130, 200),  2: (130, 200),  3: (130, 200),  4: (130, 200),  5: (130, 200),  
         6: (130, 200),  7: (130, 200),  8: (130, 200),  9: (130, 200), 10: (130, 200),  
        11: (130, 200), 12: (110, 200), 13: (110, 200), 14: (90, 200), 15: (90, 200), 
        16: (70, 220),  17: (70, 220),  18: (70, 220),  19: (60, 220),  20: (60, 220),
    },

}

sku_to_second_fontsize_placement = {  # (font-size, x, y)
    
    # customizable
    'JMUG11WBUVPPSLNTBBUVP': {     
         1: (200, 200),  2: (200, 200),  3: (200, 200),  4: (200, 200),  5: (200, 200),  
         6: (200, 200),  7: (200, 200),  8: (200, 200),  9: (200, 200), 10: (180, 210),  
        11: (180, 210), 12: (150, 230), 13: (150, 230), 14: (120, 250), 15: (120, 250), 
        16: (120, 250), 17: (100, 270), 18: (100, 270), 19: (80, 300),  20: (80, 300),
    },
    'JMUG11WBUVPPSICG1UVP': {     
         1: (200, 200),  2: (200, 200),  3: (200, 200),  4: (200, 200),  5: (200, 200),  
         6: (200, 200),  7: (200, 200),  8: (200, 200),  9: (200, 200), 10: (180, 210),  
        11: (150, 230), 12: (150, 230), 13: (120, 250), 14: (120, 250), 15: (120, 250), 
        16: (120, 250), 17: (100, 270), 18: (80, 300), 19: (80, 300),  20: (80, 300),
    },
    'JMUG11WBUVPPSNNCMUVP': {     
         1: (200, 150),  2: (200, 150),  3: (200, 150),  4: (200, 150),  5: (200, 150),  
         6: (200, 150),  7: (200, 150),  8: (200, 150),  9: (200, 150), 10: (180, 160),  
        11: (180, 160), 12: (150, 180), 13: (150, 180), 14: (120, 200), 15: (120, 200), 
        16: (120, 200), 17: (100, 220), 18: (100, 220), 19: (80, 250),  20: (80, 250),
    },
    'JMUG11WBUVPPSSBFRUVP': {     
         1: (85, 455),  2: (85, 455),  3: (85, 455),  4: (85, 455),  5: (85, 455),  
         6: (85, 455),  7: (85, 455),  8: (85, 455),  9: (85, 455), 10: (85, 455),  
        11: (85, 455), 12: (85, 455), 13: (85, 455), 14: (85, 455), 15: (85, 455), 
        16: (70, 465), 17: (70, 465), 18: (70, 465), 19: (70, 465), 20: (70, 465),
        21: (60, 475), 22: (60, 475), 23: (60, 475), 24: (50, 485), 25: (50, 485),
    },
    'JMUG11WBUVPJMCCAS2UVP': {     
         1: (150, 350),   2: (150, 350),   3: (150, 350),   4: (150, 350),   5: (150, 350),  
         6: (150, 350),   7: (150, 350),   8: (150, 350),   9: (130, 360),  10: (130, 360),       
        11: (130, 360), 12: (130, 360), 13: (110, 370), 14: (110, 370), 15: (110, 370), 
        16: (110, 370), 17: (100, 370), 18: (100, 370), 19: (100, 370), 20: (100, 370),
        21: (80, 380), 22: (80, 380), 23: (80, 380), 24: (80, 380), 25: (80, 380), 
        26: (70, 380), 27: (70, 380), 28: (60, 380), 29: (55, 380), 30: (50, 380), 
        31: (50, 380), 32: (40, 390), 33: (40, 390), 34: (30, 390), 35: (30, 390),
    },
    'JMUG11WBUVPJMCCAS3UVP': {     
         1: (150, 250),   2: (150, 250),   3: (150, 250),   4: (150, 250),   5: (150, 250),  
         6: (150, 250),   7: (150, 250),   8: (150, 250),   9: (130, 260),  10: (130, 260),       
        11: (130, 260), 12: (130, 260), 13: (110, 270), 14: (110, 270), 15: (110, 270), 
        16: (110, 270), 17: (100, 270), 18: (100, 270), 19: (100, 270), 20: (100, 270),
        21: (80, 280), 22: (80, 280), 23: (80, 280), 24: (80, 280), 25: (80, 280), 
        26: (70, 280), 27: (70, 280), 28: (60, 280), 29: (55, 280), 30: (50, 280), 
        31: (50, 280), 32: (40, 290), 33: (40, 290), 34: (30, 290), 35: (30, 290),
    },
    'JMUG11WBUVPJMCCTNR2UVP': {     
         1: (150, 350), 2: (150, 350), 3: (150, 350), 4: (150, 350),  5: (150, 350),  
         6: (150, 350), 7: (150, 350), 8: (150, 350), 9: (130, 360), 10: (130, 360),       
        11: (130, 360), 12: (130, 360), 13: (110, 370), 14: (110, 370), 15: (110, 370), 
        16: (110, 370), 17: (100, 370), 18: (100, 370), 19: (100, 370), 20: (100, 370),
        21: (80, 380), 22: (80, 380), 23: (80, 380), 24: (80, 380), 25: (80, 380), 
        26: (70, 380), 27: (70, 380), 28: (60, 380), 29: (55, 380), 30: (50, 380), 
        31: (50, 380), 32: (40, 390), 33: (40, 390), 34: (30, 390), 35: (30, 390),
    },
    'JMUG11WBUVPJMCCTNR3UVP': {     
         1: (150, 250),   2: (150, 250),   3: (150, 250),   4: (150, 250),   5: (150, 250),  
         6: (150, 250),   7: (150, 250),   8: (150, 250),   9: (130, 260),  10: (130, 260),       
        11: (130, 260), 12: (130, 260), 13: (110, 270), 14: (110, 270), 15: (110, 270), 
        16: (110, 270), 17: (100, 270), 18: (100, 270), 19: (100, 270), 20: (100, 270),
        21: (80, 280), 22: (80, 280), 23: (80, 280), 24: (80, 280), 25: (80, 280), 
        26: (70, 280), 27: (70, 280), 28: (60, 280), 29: (55, 280), 30: (50, 280), 
        31: (50, 280), 32: (40, 290), 33: (40, 290), 34: (30, 290), 35: (30, 290),
    },
    'JMUG11WBUVPJMCCDS2UVP': {     
         1: (150, 350), 2: (150, 350), 3: (150, 350), 4: (150, 350),  5: (150, 350),  
         6: (150, 350), 7: (150, 350), 8: (150, 350), 9: (130, 360), 10: (130, 360),       
        11: (130, 360), 12: (130, 360), 13: (110, 370), 14: (110, 370), 15: (110, 370), 
        16: (110, 370), 17: (100, 370), 18: (100, 370), 19: (100, 370), 20: (100, 370),
        21: (80, 380), 22: (80, 380), 23: (80, 380), 24: (80, 380), 25: (80, 380), 
        26: (70, 380), 27: (70, 380), 28: (60, 380), 29: (55, 380), 30: (50, 380), 
        31: (50, 380), 32: (40, 390), 33: (40, 390), 34: (30, 390), 35: (30, 390),
    },
    'JMUG11WBUVPJMCCDS3UVP': {     
         1: (150, 250),   2: (150, 250),   3: (150, 250),   4: (150, 250),   5: (150, 250),  
         6: (150, 250),   7: (150, 250),   8: (150, 250),   9: (130, 260),  10: (130, 260),       
        11: (130, 260), 12: (130, 260), 13: (110, 270), 14: (110, 270), 15: (110, 270), 
        16: (110, 270), 17: (100, 270), 18: (100, 270), 19: (100, 270), 20: (100, 270),
        21: (80, 280), 22: (80, 280), 23: (80, 280), 24: (80, 280), 25: (80, 280), 
        26: (70, 280), 27: (70, 280), 28: (60, 280), 29: (55, 280), 30: (50, 280), 
        31: (50, 280), 32: (40, 290), 33: (40, 290), 34: (30, 290), 35: (30, 290),
    },
    'JMUG11WBUVPPSTYBMUVP': {     
         1: (50, 450, 400),  2: (50, 450, 400),  3: (50, 450, 400),  4: (50, 450, 400),  5: (50, 450, 400),  
         6: (50, 450, 400),  7: (40, 450, 400),  8: (40, 450, 400),  9: (30, 450, 410), 10: (30, 450, 410),  
        11: (25, 450, 410), 12: (25, 450, 410), 13: (25, 450, 410), 14: (20, 450, 415), 15: (20, 450, 415), 
    },
    'JMUG11WBUVPPSSBNALUVP': {     
         1: (180, 400),  2: (180, 400),  3: (180, 400),  4: (180, 400),  5: (180, 400),  
         6: (180, 400),  7: (180, 400),  8: (180, 400),  9: (180, 400), 10: (160, 410),  
        11: (160, 410), 12: (130, 430), 13: (130, 430), 14: (100, 450), 15: (100, 450), 
        16: (100, 450), 17: (80, 470),  18: (80, 470),  19: (60, 500),  20: (60, 500),
    },

    # fav child
    'JMUG11WBUVPPS2FAVCHUVP': {     
         1: (135, 210),  2: (135, 210), 3: (135, 210), 4: (135, 210),  5: (135, 210),  
         6: (135, 210),  7: (135, 210), 8: (135, 210), 9: (135, 210), 10: (120, 220),  
        11: (120, 220), 12: (120, 240), 13: (90, 240), 14: (80, 260),  15: (80, 260), 
    },
    'JMUG11WBUVPPS3FAVCHUVP': {     
         1: (110, 210),  2: (110, 210),  3: (110, 210),  4: (110, 210),  5: (110, 210),  
         6: (110, 210),  7: (110, 210),  8: (110, 210),  9: (110, 210), 10: (110, 210),  
        11: (100, 210), 12: (100, 210), 13: (100, 210), 14: (100, 210), 15: (100, 210), 
    },
    'JMUG11WBUVPPS4FAVCHUVP': {     
         1: (110, 160), 2: (110, 160), 3: (110, 160), 4: (110, 160),  5: (110, 160),  
         6: (110, 160), 7: (110, 160), 8: (110, 160), 9: (110, 160), 10: (110, 160),  
        11: (100, 150), 12: (100, 150), 13: (100, 150), 14: (90, 155),  15: (90, 155), 
    },
}

sku_to_third_fontsize_placement = {  # (font-size, x, y)
    
    # customizable
    'JMUG11WBUVPPSNNCMUVP': {     
         1: (100, 200),  2: (100, 500),  3: (100, 200),  4: (100, 500),  5: (100, 200),  
         6: (100, 200),  7: (100, 200),  8: (100, 200),  9: (100, 200), 10: (80, 210),  
        11: (80, 210), 12: (50, 230), 13: (50, 230), 14: (20, 250), 15: (20, 250), 
        16: (20, 250), 17: (20, 270), 18: (20, 270), 19: (20, 300),  20: (20, 300),
    },
    'JMUG11WBUVPPSSBFRUVP': {     
         1: (85, 580),  2: (85, 580),  3: (85, 580),  4: (85, 580),  5: (85, 580),  
         6: (85, 580),  7: (85, 580),  8: (85, 580),  9: (85, 580), 10: (85, 580),  
        11: (85, 580), 12: (85, 580), 13: (85, 580), 14: (85, 580), 15: (85, 580), 
        16: (70, 590), 17: (70, 590), 18: (70, 590), 19: (70, 590), 20: (70, 590),
        21: (60, 600), 22: (60, 600), 23: (60, 600), 24: (50, 610), 25: (50, 610),
    },
    'JMUG11WBUVPJMCCAS3UVP': {     
         1: (150, 450),   2: (150, 450),   3: (150, 450),   4: (150, 450),   5: (150, 450),  
         6: (150, 450),   7: (150, 450),   8: (150, 450),   9: (130, 460),  10: (130, 460),       
        11: (130, 460), 12: (130, 460), 13: (110, 470), 14: (110, 470), 15: (110, 470), 
        16: (110, 470), 17: (100, 470), 18: (100, 470), 19: (100, 470), 20: (100, 470),
        21: (80, 480), 22: (80, 480), 23: (80, 480), 24: (80, 480), 25: (80, 480), 
        26: (70, 480), 27: (70, 480), 28: (60, 480), 29: (55, 480), 30: (50, 480), 
        31: (50, 480), 32: (40, 490), 33: (40, 490), 34: (30, 490), 35: (30, 490),
    },
    'JMUG11WBUVPJMCCTNR3UVP': {     
         1: (150, 450),   2: (150, 450),   3: (150, 450),   4: (150, 450),   5: (150, 450),  
         6: (150, 450),   7: (150, 450),   8: (150, 450),   9: (130, 460),  10: (130, 460),       
        11: (130, 460), 12: (130, 460), 13: (110, 470), 14: (110, 470), 15: (110, 470), 
        16: (110, 470), 17: (100, 470), 18: (100, 470), 19: (100, 470), 20: (100, 470),
        21: (80, 480), 22: (80, 480), 23: (80, 480), 24: (80, 480), 25: (80, 480), 
        26: (70, 480), 27: (70, 480), 28: (60, 480), 29: (55, 480), 30: (50, 480), 
        31: (50, 480), 32: (40, 490), 33: (40, 490), 34: (30, 490), 35: (30, 490),
    },
        
    # fav child
    'JMUG11WBUVPPS3FAVCHUVP': {     
         1: (110, 310),  2: (110, 310),  3: (110, 310),  4: (110, 310),  5: (110, 310), 
         6: (110, 310),  7: (110, 310),  8: (110, 310),  9: (110, 310), 10: (110, 310),  
        11: (100, 310), 12: (100, 310), 13: (100, 310), 14: (100, 310), 15: (100, 310), 
    },
    'JMUG11WBUVPPS4FAVCHUVP': {     
         1: (110, 250), 2: (110, 250), 3: (110, 250), 4: (110, 250),  5: (110, 250),  
         6: (110, 250), 7: (110, 250), 8: (110, 250), 9: (110, 250), 10: (110, 250),  
        11: (100, 240), 12: (100, 240), 13: (100, 240), 14: (90, 245),  15: (90, 245), 
    },
}

sku_to_four_fontsize_placement = {  # (font-size, x, y)
    'JMUG11WBUVPPS4FAVCHUVP': {     
         1: (110, None, 350), 2: (110, None, 350), 3: (110, None, 350), 4: (110, None, 350),  5: (110, None, 350),  
         6: (110, None, 350), 7: (110, None, 350), 8: (110, None, 350), 9: (110, None, 350), 10: (110, None, 350),   
        11: (100, None, 340), 12: (100, None, 340), 13: (100, None, 340), 14: (90, None, 335),  15: (90, None, 335),  
    },
}