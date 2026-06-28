# partner-targets.md  

## Vision‑Forge Partner Integration Roadmap  

| # | SaaS / API | Rationale (why it matters for Vision‑Forge) | Free‑Tier Limits (as of 2026‑06) | Integration Effort* | Primary User Job Solved | Affiliate / Revenue‑Share Program |
|---|------------|--------------------------------------------|--------------------------------|----------------------|--------------------------|-----------------------------------|
| 1 | **AWS Rekognition** | Industry‑grade object detection & facial analysis that can be called as a fallback when custom models miss. Leverages existing AWS accounts of enterprise customers. | 5,000 images/month free (up to 1 GB) + 1 hour of video analysis | **M** – SDK wrapper + IAM role handling | “Run high‑accuracy detection without training own model” | AWS Partner Network (APN) – 10 % revenue share on billed usage |
| 2 | **Google Cloud Vision API** | Provides OCR, landmark, logo, and safe‑search detection – expands Vision‑Forge beyond generic objects. | 1,000 units/month free (includes 1 k label detection, 1 k OCR) | **M** – OAuth2 flow + gRPC wrapper | “Extract text & metadata from images for downstream pipelines” | Google Cloud Partner Advantage – up‑to 15 % referral credit |
| 3 | **Azure Computer Vision** | Complements GCP offering with strong video‑indexer and spatial analysis for Azure‑centric customers. | 5,000 transactions/month free (includes OCR, object detection) | **M** – Azure AD auth + REST wrapper | “Batch‑process video streams for object tracking” | Microsoft Partner Network – 8 % revenue share on Azure consumption |
| 4 | **Roboflow API** | Hosted model‑hosting & dataset versioning; provides ready‑to‑use YOLO, EfficientDet, and custom model endpoints. Ideal for rapid prototyping. | 100 inferences/month free, 1 GB storage | **S** – Simple REST endpoint integration | “Deploy custom trained models without managing infra” | Roboflow Partner Program – 12 % of paid usage for referrals |
| 5 | **Scale AI (Nucleus) Data Labeling** | High‑quality human‑in‑the‑loop labeling for training data; integrates directly with Vision‑Forge annotation UI. | 500 images free per project | **M** – Webhook + SDK for task creation | “Generate labeled datasets to improve detection accuracy” | Scale AI Referral – 5 % of contract value |
| 6 | **Labelbox** | Collaborative labeling platform with active‑learning loops; can feed back into Vision‑Forge model training pipeline. | 1,000 labels/month free (community tier) | **M** – GraphQL API + webhook sync | “Iteratively improve model performance via active learning” | Labelbox Partner – 10 % revenue share on paid seats |
| 7 | **Hugging Face Inference API** | Access to thousands of community‑trained vision models (e.g., SAM, CLIP) for niche domains (medical, satellite). | 30 k tokens/month free (≈ 1 M pixels) | **S** – HTTP wrapper + model selector UI | “Add domain‑specific detection without training from scratch” | Hugging Face Partner – 5 % of paid compute credits |
| 8 | **Weights & Biases (W&B) MLOps** | Experiment tracking, model versioning, and performance dashboards; integrates with Vision‑Forge training jobs. | 100 GB storage, 5 GB logs/month free | **L** – SDK instrumentation + CI/CD hooks | “Monitor model drift & benchmark new model releases” | W&B Referral – 7 % of paid seat revenue |

\* **Effort Scale**:  
- **S** – < 2 weeks, single‑developer, pure REST/HTTP wrapper.  
- **M** – 2‑4 weeks, requires auth flow, SDK, or webhook orchestration.  
- **L** – > 4 weeks, multi‑service orchestration, UI extensions, CI/CD integration.

---

## Phased Integration Timeline  

| Quarter | Target(s) | Milestones |
|---------|-----------|------------|
| **Q1 2026** | 1️⃣ AWS Rekognition, 2️⃣ Google Cloud Vision, 4️⃣ Roboflow | • Build unified “External Detector” abstraction layer.<br>• Publish SDK wrappers & docs.<br>• Secure affiliate links & embed referral tracking. |
| **Q2 2026** | 3️⃣ Azure Computer Vision, 7️⃣ Hugging Face Inference | • Add video‑indexer module & SAM‑based segmentation UI.<br>• Enable model‑selector dropdown for domain‑specific APIs.<br>• Negotiate revenue‑share contracts. |
| **Q3 2026** | 5️⃣ Scale AI, 6️⃣ Labelbox | • Integrate labeling task creation from Vision‑Forge UI.<br>• Implement active‑learning loop that auto‑queues low‑confidence detections for human review.<br>• Launch joint marketing co‑sell webinars. |
| **Q4 2026** | 8️⃣ Weights & Biases | • Instrument training pipelines for experiment logging.<br>• Provide drift‑detection dashboards to enterprise customers.<br>• Release “Enterprise Monitoring” add‑on (paid). |

---

### Prioritization Logic  

1. **Revenue‑share potential** – AWS, GCP, Azure, Roboflow, Scale AI, Labelbox, W&B all have formal partner programs that pay per‑usage or per‑seat referral.  
2. **Free‑tier coverage** – Early adopters can test Vision‑Forge end‑to‑end without incurring cost, driving faster conversion.  
3. **Strategic coverage** – By spanning the three major cloud providers plus specialist labeling & model‑hosting services, Vision‑Forge becomes cloud‑agnostic and attractive to a broader developer base.  
4. **Effort vs. impact** – S‑effort integrations (Roboflow, Hugging Face) are slated early to deliver immediate value‑add, while L‑effort (W&B) is deferred to Q4 when core detection pipelines are stable.  

---  

*Prepared by Business‑Synthesis – Vision‑Forge partner targeting.*