from . import loadDefaultParams as dp
from . import timeIntegration as ti
from ..model import Model


class WCModel(Model):
    """
    The two-population Wilson-Cowan model
    """

    name = "wc"
    description = "Wilson-Cowan model"

    init_vars = ["exc_init", "inh_init", "exc_ou", "inh_ou"]
    state_vars = ["exc", "inh", "exc_ou", "inh_ou", "brackets_E", "brackets_I"]
    output_vars = ["exc", "inh", "brackets_E", "brackets_I"]
    default_output = "exc"
    input_vars = ["exc_ext", "inh_ext", "control_term_E", "control_term_I"]
    default_input = "exc_ext"

    # because this is not a rate model, the input
    # to the bold model must be transformed
    boldInputTransform = lambda self, x: x * 50

    def __init__(self, params=None, Cmat=None, Dmat=None, seed=None):

        self.Cmat = Cmat
        self.Dmat = Dmat
        self.seed = seed

        # the integration function must be passed
        integration = ti.timeIntegration

        # load default parameters if none were given
        if params is None:
            params = dp.loadDefaultParams(Cmat=self.Cmat, Dmat=self.Dmat, seed=self.seed)

        # Initialize base class Model
        super().__init__(integration=integration, params=params)
