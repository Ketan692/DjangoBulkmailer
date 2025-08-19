from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError
from django.contrib import messages
from .forms import BulkEmailForm
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

@login_required
def homepage(request):
    sender_email = request.user.email
    sender_name = request.user.get_full_name() or request.user.username

    if request.method == 'POST':
        form = BulkEmailForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            recipients_raw = form.cleaned_data['recipients']

            valid_recipients = []
            invalid_recipients = []

            for email in recipients_raw.replace('\n', ',').split(','):
                email = email.strip()
                if not email:
                    continue
                try:
                    validate_email(email)
                    valid_recipients.append(email)
                except ValidationError:
                    invalid_recipients.append(email)

            if invalid_recipients:
                messages.warning(
                    request, 
                    f"⚠️ These emails are invalid and will be skipped: {', '.join(invalid_recipients)}"
                )

            if not valid_recipients:
                messages.error(request, "❌ No valid recipient emails provided.")
                return redirect('homepage')

            message_body = f"""
Dear Recipient,

{content}

If you have any questions or need further information, please don't hesitate to reach out.

Best regards,  
{sender_name}  
{sender_email}
"""

            try:
                email = EmailMessage(
                    subject=subject,
                    body=message_body,
                    from_email=sender_email,
                    to=valid_recipients,
                    cc=[sender_email],
                    reply_to=[sender_email],
                )
                email.send(fail_silently=False)
                messages.success(request, "✅ Emails sent successfully!")
            except BadHeaderError:
                messages.error(request, "❌ Invalid header found.")
            except Exception as e:
                messages.error(request, f"❌ An error occurred: {str(e)}")

            return redirect('homepage')

        else:
            # Form is invalid: show errors
            return render(request, 'home/homepage.html', {
                'form': form,
                'sender_email': sender_email,
            })

    else:
        # GET request: show empty form
        form = BulkEmailForm()
        return render(request, 'home/homepage.html', {
            'form': form,
            'sender_email': sender_email,
        })
