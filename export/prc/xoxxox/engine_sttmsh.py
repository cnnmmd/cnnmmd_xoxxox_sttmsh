import numpy as np
from moonshine_voice import Transcriber, get_model_for_language
from xoxxox.shared import Custom
from xoxxox.params import Medium

#---------------------------------------------------------------------------

class SttPrc():

  def __init__(self, config="xoxxox/config_sttmsh_000", **dicprm):
    diccnf = Custom.update(config, dicprm)
    lngtgt = diccnf["lngtgt"]
    pthprm, arcprm = get_model_for_language(lngtgt)
    self.nmodel = Transcriber(model_path=pthprm, model_arch=arcprm)

  def infere(self, datpcm):
    datnom = np.frombuffer(datpcm, dtype=np.float32).tolist()
    objres = self.nmodel.transcribe_without_streaming(datnom, sample_rate=Medium.ratsmp)
    #print(objres.lines, flush=True) # DBG
    txtres = "\n".join(l.text for l in objres.lines if l.text)
    print(txtres, flush=True) # DBG
    return txtres
