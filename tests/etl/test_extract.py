import pytest

from etl.extract import load_data


class TestLoadData:
    def test_happy_path_load_data(self):
        _ = load_data(year=2022, month=1)

    @pytest.mark.parametrize("year", [2021, 2022])
    @pytest.mark.parametrize("month", [10, 11])
    def test_load_data_value_error(self, year, month):
        with pytest.raises(
            ValueError,
            match=f"^Data for year {year:04d} and month {month:02d} not found on the data folder$",
        ):
            _ = load_data(year=year, month=month)
