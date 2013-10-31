from ert_gui.ide.keywords.definitions import IntegerArgument, KeywordDefinition, ConfigurationLineDefinition, PathArgument, StringArgument, FloatArgument, BoolArgument


class EnkfControlKeywords(object):
    def __init__(self, ert_keywords):
        super(EnkfControlKeywords, self).__init__()
        self.group = "Enkf Control"

        ert_keywords.addKeyword(self.addEnkfAlpha())
        ert_keywords.addKeyword(self.addEnkfBootstrap())
        ert_keywords.addKeyword(self.addEnkfCvFolds())
        ert_keywords.addKeyword(self.addEnkfForceNComp())
        ert_keywords.addKeyword(self.addEnkfLocalCv())
        ert_keywords.addKeyword(self.addEnkfPenPress())
        ert_keywords.addKeyword(self.addEnkfMode())
        ert_keywords.addKeyword(self.addMergeObservations())
        ert_keywords.addKeyword(self.addEnkfNComp())
        ert_keywords.addKeyword(self.addEnkfRerun())
        ert_keywords.addKeyword(self.addEnkfScaling())
        ert_keywords.addKeyword(self.addEnkfTruncation())
        ert_keywords.addKeyword(self.addUpdateLogPath())
        ert_keywords.addKeyword(self.addRerunStart())
        ert_keywords.addKeyword(self.addUpdateResults())


    def addEnkfAlpha(self):
        enkf_alpha = ConfigurationLineDefinition(keyword=KeywordDefinition("ENKF_ALPHA"),
                                                 arguments=[FloatArgument()],
                                                 documentation_link="enkf_control/enkf_alpha",
                                                 required=False,
                                                 group=self.group)
        return enkf_alpha



    def addEnkfBootstrap(self):
        enkf_bootstrap = ConfigurationLineDefinition(keyword=KeywordDefinition("ENKF_BOOTSTRAP"),
                                                     arguments=[BoolArgument()],
                                                     documentation_link="enkf_control/enkf_bootstrap",
                                                     required=False,
                                                     group=self.group)
        return enkf_bootstrap



    def addEnkfCvFolds(self):
        enkf_cv_folds = ConfigurationLineDefinition(keyword=KeywordDefinition("ENKF_CV_FOLDS"),
                                                    arguments=[IntegerArgument()],
                                                    documentation_link="enkf_control/enkf_cv_folds",
                                                    required=False,
                                                    group=self.group)
        return enkf_cv_folds



    def addEnkfForceNComp(self):
        enkf_force_ncomp = ConfigurationLineDefinition(keyword=KeywordDefinition("ENKF_FORCE_NCOMP"),
                                                    arguments=[BoolArgument()],
                                                    documentation_link="enkf_control/enkf_force_ncomp",
                                                    required=False,
                                                    group=self.group)
        return enkf_force_ncomp


    def addEnkfLocalCv(self):
        enkf_local_cv = ConfigurationLineDefinition(keyword=KeywordDefinition("ENKF_LOCAL_CV"),
                                                    arguments=[BoolArgument()],
                                                    documentation_link="enkf_control/enkf_local_cv",
                                                    required=False,
                                                    group=self.group)
        return enkf_local_cv


    def addEnkfPenPress(self):
        enkf_pen_press = ConfigurationLineDefinition(keyword=KeywordDefinition("ENKF_PEN_PRESS"),
                                                    arguments=[BoolArgument()],
                                                    documentation_link="enkf_control/enkf_pen_press",
                                                    required=False,
                                                    group=self.group)
        return enkf_pen_press



    def addEnkfMode(self):
        enkf_mode = ConfigurationLineDefinition(keyword=KeywordDefinition("ENKF_MODE"),
                                                    arguments=[StringArgument(built_in=True)],
                                                    documentation_link="enkf_control/enkf_mode",
                                                    required=False,
                                                    group=self.group)
        return enkf_mode



    def addMergeObservations(self):
        enkf_merge_observations = ConfigurationLineDefinition(keyword=KeywordDefinition("ENKF_MERGE_OBSERVATIONS"),
                                                    arguments=[BoolArgument()],
                                                    documentation_link="enkf_control/enkf_merge_observations",
                                                    required=False,
                                                    group=self.group)
        return enkf_merge_observations



    def addEnkfNComp(self):
        enkf_ncomp = ConfigurationLineDefinition(keyword=KeywordDefinition("ENKF_NCOMP"),
                                                 arguments=[IntegerArgument()],
                                                 documentation_link="enkf_control/enkf_ncomp",
                                                 required=False,
                                                 group=self.group)
        return enkf_ncomp


    def addEnkfRerun(self):
        enkf_rerun = ConfigurationLineDefinition(keyword=KeywordDefinition("ENKF_RERUN"),
                                                 arguments=[BoolArgument()],
                                                 documentation_link="enkf_control/enkf_rerun",
                                                 required=False,
                                                 group=self.group)
        return enkf_rerun


    def addRerunStart(self):
        rerun_start = ConfigurationLineDefinition(keyword=KeywordDefinition("RERUN_START"),
                                                 arguments=[IntegerArgument()],
                                                 documentation_link="enkf_control/rerun_start",
                                                 required=False,
                                                 group=self.group)
        return rerun_start



    def addEnkfScaling(self):
        enkf_scaling = ConfigurationLineDefinition(keyword=KeywordDefinition("ENKF_SCALING"),
                                                   arguments=[BoolArgument()],
                                                   documentation_link="enkf_control/enkf_scaling",
                                                   required=False,
                                                   group=self.group)
        return enkf_scaling



    def addEnkfTruncation(self):
        enkf_truncation = ConfigurationLineDefinition(keyword=KeywordDefinition("ENKF_TRUNCATION"),
                                                      arguments=[FloatArgument()],
                                                      documentation_link="enkf_control/enkf_truncation",
                                                      required=False,
                                                      group=self.group)
        return enkf_truncation



    def addUpdateLogPath(self):
        update_log_path = ConfigurationLineDefinition(keyword=KeywordDefinition("UPDATE_LOG_PATH"),
                                                      arguments=[PathArgument()],
                                                      documentation_link="enkf_control/update_log_path",
                                                      required=False,
                                                      group=self.group)
        return update_log_path


    def addUpdateResults(self):
        update_results = ConfigurationLineDefinition(keyword=KeywordDefinition("UPDATE_RESULTS"),
                                                     arguments=[BoolArgument()],
                                                     documentation_link="enkf_control/update_results",
                                                     required=False,
                                                     group=self.group)
        return update_results
