import pandas as pd
from django.conf import settings
from django.shortcuts import render
from .dashboard import frequency_table


def dashboard_view(request):
    """Main dashboard view that loads vehicle data and renders charts."""
    csv_path = settings.BASE_DIR / "dummy_data" / "vehicles_data_1000.csv"
    queryset = pd.read_csv(csv_path)
    df = pd.DataFrame(queryset)

    return render(request, "vehicles/index.html", {
        "frequency_table": frequency_table(df),
    })
