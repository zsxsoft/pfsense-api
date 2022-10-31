"""Script used to test the /api/v1/system/package endpoint."""
import e2e_test_framework


class APIE2ETestSystemPackage(e2e_test_framework.APIE2ETest):
    """Class used to test the /api/v1/system/package endpoint."""
    uri = "/api/v1/system/package"
    get_tests = [{"name": "Read installed packages"}]
    post_tests = [
        {
            "name": "Check install of pfSense repo package",
            "resp_time": 30,
            "req_data": {
                "name": "pfSense-pkg-nmap"
            }
        },
        {
            "name": "Check package name required constraint",
            "status": 400,
            "return": 1073
        },
        {
            "name": "Check inability to install already installed package",
            "status": 400,
            "return": 1076,
            "resp_time": 30,
            "req_data": {
                "name": "pfSense-pkg-nmap"
            }
        },
        {
            "name": "Check install package from pfSense repo that doesn't exist",
            "status": 400,
            "return": 1075,
            "resp_time": 5,
            "req_data": {
                "name": "pfSense-pkg-INVALID"
            }
        },

    ]
    delete_tests = [
            {
                "name": "Test deletion of installed package",
                "resp_time": 30,
                "req_data": {
                    "name": "pfSense-pkg-nmap"
                }
            },
            {
                "name": "Check package name required constraint",
                "status": 400,
                "return": 1073
            },
            {
                "name": "Check inability to delete system packages, only pfSense packages",
                "status": 400,
                "return": 1074,
                "req_data": {
                    "name": "sudo"
                }
            }
        ]


APIE2ETestSystemPackage()
