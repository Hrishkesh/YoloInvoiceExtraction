
def pdf2img(pdfinp, outfile):
    
    from glob import glob
    from PIL import Image
    import os
    import sys
    from pdf2image import convert_from_path

    path_pdf = glob(pdfinp +  r'\\*.pdf')


    if os.path.exists(outfile):
        pass
    else:
        os.mkdir(outfile)

    for i, file in enumerate(path_pdf):
        pages = convert_from_path(file,300, poppler_path = r'C:\\Users\\hpattepu\\AppData\\Local\\Continuum\\anaconda3\\envs\\RPA\\poppler-0.68.0\\bin') 
        for j, page in enumerate(pages):
            file = os.path.basename(file)
            file = file.split('.pdf')[0]
            output = outfile + r'\\image' + str(i) + r'.jpg'
            page.save(output,'JPEG')
           
    return "Completed processing pdf"
        


        

