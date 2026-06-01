@property
def state(self):
    if not self.coordinator.data:
        return "unknown"

    # 🔥 FULL JSON OUTPUT ALS STRING
    import json
    return json.dumps(self.coordinator.data)
