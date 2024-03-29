def global_styles(request):
    return {
        "PRIMARY_BUTTON": "text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none "
                          "focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 "
                          "text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
    }


def image_transformations(request):
    return dict(
        ANIMAL_THUMB=dict(
            format="png",
            transformation=[
                "pet"
            ],
            sign_url="true"
        )
    )
