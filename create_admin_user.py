from Main.models import User, AdminUsers

# Check if a user with ID 1 already exists
user_id = 1
try:
    user = User.objects.get(pk=user_id)
    print("User with ID 1 already exists.")
except User.DoesNotExist:
    # If user with ID 1 doesn't exist, you may need to create one first or handle the case accordingly
    print("User with ID 1 does not exist. Please create it first.")

# Now create an AdminUser instance with the User instance
admin_user = AdminUsers.objects.create(user=user)  # Fill in with your field values
print("AdminUser with user ID 1 created successfully.")
