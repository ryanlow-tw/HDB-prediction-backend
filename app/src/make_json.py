class MakeJson:

    @staticmethod
    def format_results(result):
        formatted_result = f"{result:.2f}"

        json_format = {
            "results": formatted_result
        }

        return json_format
