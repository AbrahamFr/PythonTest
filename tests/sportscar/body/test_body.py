from pytest import mark

@mark.body
class BodyTests:
    @mark.smoke
    @mark.door
    def test_body_functions_as_exected(self):
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True 