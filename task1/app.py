import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# ===== Load Data =====
df_product = pd.read_csv("task1/data/avg_by_product.csv")
df_server = pd.read_csv("task1/data/avg_by_server.csv")
df_month = pd.read_csv("task1/data/avg_by_month.csv")

df_month["month"] = pd.to_datetime(df_month["month"])

# ===== Generate Charts =====

# 1. Product chart
plt.figure(figsize=(6,4))
df_product.sort_values("avg_resolution_days", inplace=True)
plt.barh(df_product["product"], df_product["avg_resolution_days"], color="skyblue")
plt.xlabel("Avg Resolution Days")
plt.title("Average Resolution by Product")
plt.tight_layout()
plt.savefig("task1/data/chart_product.png")
plt.close()

# 2. Monthly trend chart
plt.figure(figsize=(6,4))
plt.plot(df_month["month"], df_month["avg_resolution_days"], marker="o", color="green")
plt.xlabel("Month")
plt.ylabel("Avg Resolution Days")
plt.title("Monthly Resolution Trend")
plt.tight_layout()
plt.savefig("task1/data/chart_month.png")
plt.close()

# 3. Server chart
plt.figure(figsize=(6,4))
df_server_sorted = df_server.sort_values("avg_resolution_days", ascending=False)
plt.bar(df_server_sorted["server"], df_server_sorted["avg_resolution_days"], color="orange")
plt.xlabel("Server")
plt.ylabel("Avg Resolution Days")
plt.title("Average Resolution by Server")
plt.tight_layout()
plt.savefig("task1/data/chart_server.png")
plt.close()

# ===== Insights =====
insights = []

slowest_product = df_product.loc[df_product["avg_resolution_days"].idxmax()]
fastest_product = df_product.loc[df_product["avg_resolution_days"].idxmin()]
insights.append(f"📌 Product Insight: {slowest_product['product']} complaints take the longest "
                f"({slowest_product['avg_resolution_days']} days), while {fastest_product['product']} is faster "
                f"({fastest_product['avg_resolution_days']} days).")

worst_server = df_server.loc[df_server["avg_resolution_days"].idxmax()]
best_server = df_server.loc[df_server["avg_resolution_days"].idxmin()]
insights.append(f"📌 Server Insight: Server {worst_server['server']} is the slowest "
                f"({worst_server['avg_resolution_days']} days avg), while {best_server['server']} is the fastest "
                f"({best_server['avg_resolution_days']} days).")

peak_month = df_month.loc[df_month["avg_resolution_days"].idxmax()]
low_month = df_month.loc[df_month["avg_resolution_days"].idxmin()]
insights.append(f"📌 Trend Insight: Resolution peaked in {peak_month['month'].strftime('%b %Y')} "
                f"({peak_month['avg_resolution_days']} days) but improved by {low_month['month'].strftime('%b %Y')} "
                f"({low_month['avg_resolution_days']} days).")

# ===== Build PDF =====
doc = SimpleDocTemplate("task1/Complaint_Resolution_Report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

story.append(Paragraph("<b>Complaint Resolution Analysis Report</b>", styles["Title"]))
story.append(Spacer(1, 20))

story.append(Paragraph("Average Resolution by Product", styles["Heading2"]))
story.append(Image("task1/data/chart_product.png", width=400, height=300))
story.append(Spacer(1, 12))

story.append(Paragraph("Monthly Trend of Resolution Time", styles["Heading2"]))
story.append(Image("task1/data/chart_month.png", width=400, height=300))
story.append(Spacer(1, 12))

story.append(Paragraph("Average Resolution by Server", styles["Heading2"]))
story.append(Image("task1/data/chart_server.png", width=400, height=300))
story.append(Spacer(1, 12))

story.append(Paragraph("<b>Insights</b>", styles["Heading2"]))
for i in insights:
    story.append(Paragraph(i, styles["Normal"]))
    story.append(Spacer(1, 10))

doc.build(story)

print("✅ PDF report generated: task1/Complaint_Resolution_Report.pdf")
