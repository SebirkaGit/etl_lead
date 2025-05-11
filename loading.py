def load(targetfile, data_to_load):
    data_to_load.to_csv(targetfile)

    targetfile = "transformed_data.csv"

    load(targetfile, transformed_data)