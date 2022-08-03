from sample.controller import SampleController


class SampleResource:
    @staticmethod
    @ValidateParams()
    def get():
        return SampleController.get_sample_list()
