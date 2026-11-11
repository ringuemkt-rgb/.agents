import importlib.util,json,sys,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]
S=importlib.util.spec_from_file_location("lesson_planner",P/"src"/"lesson_planner.py")
M=importlib.util.module_from_spec(S);sys.modules[S.name]=M;S.loader.exec_module(M)
class LessonTests(unittest.TestCase):
    def r(self,**extra):
        x={"class_id":"fitbox-boxe-matutino","start_time":"06:00","duration_min":40}
        x.update(extra);return x
    def test_correct_duration(self):
        x=M.generate(self.r());self.assertEqual(x["end"],"06:40")
        self.assertEqual(sum(z["duration_min"] for z in x["stages"]),40)
    def test_reject_unconfirmed_schedule(self):
        with self.assertRaises(ValueError):M.generate(self.r(start_time="17:00"))
    def test_reject_contact(self):
        with self.assertRaises(ValueError):M.generate(self.r(contact=True))
    def test_12_week_curriculum(self):
        for w in range(1,13):
            for s in (1,2):
                self.assertEqual(len(M.generate(self.r(week=w,session=s))["stages"]),6)
    def test_output_svg(self):
        self.assertIn("<svg",M.render_html(M.generate(self.r())))
    def test_50minute_request_not_default(self):
        self.assertEqual(M.generate({"class_id":"ctrk-boxe-meiodia","start_time":"12:00","duration_min":50})["end"],"12:50")
    def test_no_personal_data(self):
        self.assertNotIn("@",str(P.joinpath("README.md").read_text()))
if __name__=="__main__":unittest.main()
