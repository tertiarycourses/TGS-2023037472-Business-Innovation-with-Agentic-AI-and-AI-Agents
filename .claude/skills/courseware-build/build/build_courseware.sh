#!/usr/bin/env bash
# v41 single-command build: deck -> LP -> LG -> activity/lab folders -> bcm templates -> PDFs with page-numbered TOCs.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; REPO="$(cd "$HERE/../../../.." && pwd)"; CW="$REPO/courseware"
SHORT="$(python3 -c "import sys; sys.path.insert(0,'$HERE'); import course_data as C; print(C.SHORT_TITLE)")"
VER="$(python3 -c "import sys; sys.path.insert(0,'$HERE'); import course_data as C; print(C.VERSION)")"
python3 "$HERE/build_slides.py"
python3 "$HERE/build_lesson_plan.py"
python3 "$HERE/build_learner_guide.py"
python3 "$HERE/build_activities.py"
[ -d "$HOME/projects/edtools/bcm" ] && python3 "$HERE/export_bcm_templates.py" || true
python3 "$HERE/build_prompts_page.py"
PPT="$CW/$SHORT-$VER.pptx"; LP="$CW/LP-$SHORT.docx"; LG="$CW/LG-$SHORT.docx"
for f in "$PPT" "$LP" "$LG"; do soffice --headless --convert-to pdf --outdir "$CW" "$f" >/dev/null 2>&1; done
python3 "$HERE/inject_toc.py" "$LP" "${LP%.docx}.pdf" 2
python3 "$HERE/inject_toc.py" "$LG" "${LG%.docx}.pdf" 2
for f in "$LP" "$LG"; do soffice --headless --convert-to pdf --outdir "$CW" "$f" >/dev/null 2>&1; done
echo "==> Done"; ls -1 "$CW"/*.pptx "$CW"/*.pdf "$CW"/*.docx
