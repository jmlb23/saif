import pandas
import sys
import os


def main():
    if len(sys.argv) != 5:
        print("Usage: script.py archive.[xls | xlsx] sheet_name new_aquive_name folder_destination")
    else:
        csv = sys.argv[1]
        sheet_name = sys.argv[2]
        name = sys.argv[3]
        path = sys.argv[4]
        if not os.path.isdir(path):
            os.mkdir(path)
        csv_rows = pandas.read_excel(csv,sheet_name=sheet_name)

        for index in range(1, len(csv_rows.columns)):
            key_with_lang = csv_rows.iloc[:, [0, index]].copy()
            with_xml = key_with_lang.apply(lambda x : f'<string name="{x[0]}">{x[1]}</string>', axis=1)
            xml_lines = with_xml.tolist()
            xml_string = "\n".join(xml_lines)
            xml_stirng_root = f"<resources>\n{xml_string}\n</resources>"
            file = open(f"./{path}/{name}_{key_with_lang.columns[1]}.xml","w")
            file.write(xml_stirng_root)
            file.close()

if __name__ == "__main__":
    main()
